from app.services.elevenlabs import ElevenLabsService
import os

# elevenlabs = ElevenLabsService()
# audio_data = elevenlabs.text_to_speech("Hello, this is a test.")

# if audio_data:
#     file_path = "static/output.mp3"  # Save in a public folder
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)

#     with open(file_path, "wb") as f:
#         f.write(audio_data)
    
#     # Assume we are serving the file via Flask or another method
#     audio_url = f"http://localhost:5000/{file_path}"
#     print("Generated Audio URL:", audio_url)
# else:
#     print("Failed to generate speech.")

elevenlabs_service = ElevenLabsService()  
audio_file = elevenlabs_service.text_to_speech("Hello, this is a test.")

if isinstance(audio_file, str) and audio_file:
    print(f"Audio saved at: app/static/{audio_file}")
else:
    print("Failed to generate audio.")
