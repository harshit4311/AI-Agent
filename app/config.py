import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    TWILIO_SID = os.getenv("TWILIO_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")