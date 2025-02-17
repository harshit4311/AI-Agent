import os
from app import create_app
from flask import send_from_directory
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from twilio.rest import Client
from app.services.twilio_service import handle_twilio_call
from app.services.elevenlabs import ElevenLabsService

# load environment variables
load_dotenv()

app = Flask(__name__)
    
# Fetch credentials from .env
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

elevenlabs_service = ElevenLabsService()
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN) 


# /hello endpoint
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "hello, our API is working..."})


# /call endpoint
@app.route("/call", methods=["POST"])
def initiate_call():
    data = request.json
    to_number = data.get("to")
    text = data.get("text", "Hello! This is your AI assistant.")  # Default text

    if not to_number or not text:
        return jsonify({"error": "Missing required parameters"}), 400

    response = handle_twilio_call(to_number, text)
    return jsonify(response)

# @app.route("/call", methods=["POST"])
# def initiate_call():
#     data = request.json
#     to_number = data.get("to")  # Extract the recipient's phone number
#     text = data.get("text", "Hello! This is your AI assistant.")  # Default text if not provided

#     # Step 1: Validate input
#     if not to_number or not text:
#         return jsonify({"error": "Missing required parameters"}), 400

#     # Step 2: Generate audio using ElevenLabs
#     audio_url = elevenlabs_service.text_to_speech(text)  # Call the ElevenLabs service to generate audio
    
#     if not audio_url:
#         return jsonify({"error": "Failed to generate audio"}), 500

#     # Step 3: Create TwiML response
#     twiml_response = f"""
#     <Response>
#         <Play>{audio_url}</Play>
#     </Response>
#     """

#     # Step 4: Initiate Twilio Call
#     try:
#         call = client.calls.create(
#             to=to_number,
#             from_=TWILIO_PHONE_NUMBER,
#             twiml=twiml_response
#         )
#         return jsonify({"message": "Call initiated", "call_sid": call.sid}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# generate-audio endpoint
@app.route("/generate-audio", methods=["POST"])
def generate_audio():
    """Generate audio from text input and return the file URL."""
    data = request.get_json()
    text = data.get("text", "")
    recipient_phone = data.get("phone_number", "")

    if not text or not recipient_phone:
        return jsonify({"error": "Text and phone number required"}), 400

    output_path = "app/static/output.mp3"
    elevenlabs_service.text_to_speech(text)  # Generates output.mp3

    # Call recipient and play the generated audio
    call = client.calls.create(
        twiml=f'<Response><Play>https://8387-36-255-84-98.ngrok-free.app/static/output.mp3</Play></Response>',
        to=recipient_phone,
        from_=TWILIO_PHONE_NUMBER
    )

    return jsonify({"message": "Audio generated and call initiated", "call_sid": call.sid})



# # Serve audio files from the correct static directory
# @app.route("/app/static/<path:filename>")
# def serve_audio(filename):
#     """Serve generated audio files from the static directory."""
#     return send_from_directory("app/static", filename)
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)


@app.route("/output.mp3")
def serve_audio():
    return send_from_directory(os.path.join(os.getcwd(), "app/static"), "output.mp3", mimetype="audio/mpeg")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
    
if __name__ == "__main__":
    app.run(debug=True)