# Conversational AI-Agent
This project enables AI-powered voice calls using Flask, Twilio, and ElevenLabs. It converts text to speech and makes automated voice calls.

## Features

- Generate AI voice from text using ElevenLabs
- Make automated calls with Twilio
- Serve and access generated audio files

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Flask
- Twilio account & credentials
- ElevenLabs API key
- ngrok (to expose the local server)

## Project Setup

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```
git clone https://github.com/harshit4311/AI-Agent.git
cd AI-Agent
```

### 2. Create a Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Create a ```.env``` File in the root directory 

Example ```.env``` File
```
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

### 5. Run the Flask Server
```
python -m main.py
```
By default, the server runs at ```http://127.0.0.1:5000```.

### 6. Expose Local Server with ngrok
```
ngrok http 5000
```
Copy the ```https://your-ngrok-url.ngrok-free.app``` and update it in Twilio's webhook settings.

### 7. Testing the Endpoints (using Postman)

##### 1. ```/hello``` endpoint

Select ```GET``` method

URL:
```
http://127.0.0.1:5000/hello
```

##### 2. ```/generate-audio``` endpoint

Select ```POST``` method

URL:
```
http://127.0.0.1:5000/generate-audio
```

```JSON``` Body:
```
{
  "text": "Hello, welcome to AI calls!",
  "phone_number": "+91XXXXXXXXXX"
}
```

##### 3. ```/call``` endpoint

Select ```POST``` method

URL:
```
http://127.0.0.1:5000/call
```

```JSON``` Body:
```
{
  "to": "+91XXXXXXXXXX",
  "text": "Hello! This is your AI assistant."
}
```

## 🎥 Demo Video

Check out the demo video showcasing the AI-powered voice call functionality:

[Watch the demo video on Google Drive](https://drive.google.com/file/d/1TwLmM9v0N6xRwXoxf9bQMZ0qQyXsXN_7/view?usp=sharing)

