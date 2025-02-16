from flask import Flask
from app.routes import main # Import Blueprint
from app.config import Config
import os

def create_app():
    app = Flask(__name__)

    # # Load config
    app.config.from_object("app.config.Config")

    # Print to confirm variables are loaded (remove in production)
    print("Following are your credentials:")
    print("Twilio SID:", os.getenv("TWILIO_SID"))
    print("Twilio Auth Token:", os.getenv("TWILIO_AUTH_TOKEN"))
    print("ELEVENLABS_API_KEY:", os.getenv("ELEVENLABS_API_KEY"))  # Debugging check
    
    # Register routes
    app.register_blueprint(main)
    return app
