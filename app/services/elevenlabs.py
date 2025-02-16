import requests
import os

class ElevenLabsService:
    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.voice_id = "EXAVITQu4vr4xnSDxMaL"
        self.base_url = "https://api.elevenlabs.io/v1/text-to-speech"

        print("Using API Key:", self.api_key)  # Debugging

    def text_to_speech(self, text):
        """Converts text to speech and saves the audio file."""
        headers = {
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }
        
        data = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        response = requests.post(f"{self.base_url}/{self.voice_id}", json=data, headers=headers)

        if response.status_code == 200:
            file_path = "app/static/output.mp3"
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, "wb") as f:
                f.write(response.content)
            
            print("Audio saved as:", file_path)
            return file_path
        else:
            print("Error:", response.text)
            return None