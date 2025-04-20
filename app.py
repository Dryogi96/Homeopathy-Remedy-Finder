# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data
homeo_remedies = {
    "fever": {
        "name": "Belladonna",
        "description": "Useful for sudden high fever with red face",
        "potency": "30C"
    },
    "cold": {
        "name": "Aconite",
        "description": "For sudden cold exposure symptoms",
        "potency": "30C"
    }
}

allo_remedies = {
    "fever": {
        "name": "Paracetamol",
        "description": "For high fever and body pain",
        "dosage": "500mg every 6-8 hrs"
    },
    "cold": {
        "name": "Cetirizine",
        "description": "For cold and sneezing",
        "dosage": "10mg once daily"
    }
}

@app.route('/api/remedies/homeopathic')
def get_homeopathic():
    symptoms = request.args.get('symptoms', '').lower()
    for keyword in homeo_remedies:
        if keyword in symptoms:
            return jsonify([homeo_remedies[keyword]])
    return jsonify([]), 404

@app.route('/api/remedies/allopathic')
def get_allopathic():
    symptoms = request.args.get('symptoms', '').lower()
    for keyword in allo_remedies:
        if keyword in symptoms:
            return jsonify([allo_remedies[keyword]])
    return jsonify([]), 404

@app.route('/')
def index():
    return "HealSync Remedy API Running!"

if __name__ == '__main__':
    app.run(debug=True)
