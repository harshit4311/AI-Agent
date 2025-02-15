import requests
from app.config import Config

ELEVENLABS_API_KEY = Config.ELEVENLABS_API_KEY

def speech_to_text(audio_url):
    """Converts audio to text using ElevenLabs API"""
    response = requests.post(
        "https://api.elevenlabs.io/v1/speech-to-text",
        headers={"Authorization": f"Bearer {ELEVENLABS_API_KEY}"},
        json={"audio_url": audio_url}
    )
    return response.json().get("transcription", "")

def text_to_speech(text):
    """Converts text to speech using ElevenLabs API"""
    response = requests.post(
        "https://api.elevenlabs.io/v1/text-to-speech",
        headers={"Authorization": f"Bearer {ELEVENLABS_API_KEY}"},
        json={"text": text}
    )
    return response.json().get("audio_url", "")
