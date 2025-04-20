from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy homeopathy remedies
remedies = [
    {"name": "Belladonna", "description": "Good for high fever with red face", "potency": "30C"},
    {"name": "Aconite", "description": "Early stages of cold with anxiety", "potency": "30C"},
    {"name": "Nux Vomica", "description": "Irritability and digestive troubles", "potency": "30C"}
]

@app.route("/")
def home():
    return "HealSync Remedy API is running"

@app.route("/homeo")
def get_homeo():
    symptom = request.args.get("symptom", "")
    found = [r for r in remedies if symptom.lower() in r["description"].lower()]
    return jsonify(found or remedies)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
