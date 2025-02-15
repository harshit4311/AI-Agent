import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    TWILIO_SID = os.getenv("TWILIO_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
