# app/services/twilio_service.py

from twilio.rest import Client
import os, requests
from flask import jsonify

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def handle_twilio_call(to_number, text):
    """Initiates a call and plays the provided text as speech."""
    try:
        call = client.calls.create(
            twiml=f"<Response><Say>{text}</Say></Response>",
            to=to_number,
            from_=TWILIO_PHONE_NUMBER
        )
        return {"status": "Call initiated", "call_sid": call.sid}
    except Exception as e:
        return {"error": str(e)}


def generate_elevenlabs_audio(text):
    """ Generate speech from text using ElevenLabs API """
    url = "https://api.elevenlabs.io/v1/text-to-speech"

    headers = {
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }

    payload = {
        "voice_id": "EXAVITQu4vr4xnSDxMaL",
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "output_format": "mp3"
    }

    response = requests.post(url, json=payload, headers=headers)
    print("ElevenLabs Response:", response.text)  # Debugging log

    if response.status_code == 200:
        audio_url = response.json().get("audio_url")
        print("Generated Audio URL:", audio_url)  # Debugging log
        return audio_url
    else:
        print("Error generating audio:", response.text)
        return None
