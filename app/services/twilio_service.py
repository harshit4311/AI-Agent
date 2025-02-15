# app/services/twilio_service.py

from twilio.rest import Client
import os

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  

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