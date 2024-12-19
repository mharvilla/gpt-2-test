from flask import Blueprint, request, jsonify
from transformers import pipeline

# Load the Hugging Face GPT-2 model
generator = pipeline("text-generation", model="gpt2")

main = Blueprint("main", __name__)


@main.route("/generate", methods=["POST"])
def generate_text():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return jsonify(result)
