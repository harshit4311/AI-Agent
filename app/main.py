from app import create_app
from flask import send_from_directory
from flask import Flask, request, jsonify, send_from_directory

from app.services.elevenlabs import ElevenLabsService
elevenlabs_service = ElevenLabsService()


app = create_app()
    
@app.route("/generate-audio", methods=["POST"])
def generate_audio():
    """Generate audio from text input."""
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    output_path = "app/static/output.mp3"
    elevenlabs_service.text_to_speech(text)

    return jsonify({"message": "Audio generated", "file_url": "/static/output.mp3"})


# Serve audio files from the correct static directory
@app.route("/app/static/<path:filename>")
def serve_audio(filename):
    """Serve generated audio files from the static directory."""
    return send_from_directory("app/static", filename)

if __name__ == "__main__":
    app.run(debug=True)