from flask import Blueprint, request, jsonify
from app.services.twilio_service import handle_twilio_call

main = Blueprint("main", __name__)


# /hello endpoint
@main.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "hello, our API is working..."})


# /call endpoint
@main.route("/call", methods=["POST"])
def initiate_call():
    data = request.json
    to_number = data.get("to")
    text = data.get("text", "Hello! This is your AI assistant.")  # Default text

    if not to_number or not text:
        return jsonify({"error": "Missing required parameters"}), 400

    response = handle_twilio_call(to_number, text)
    return jsonify(response)