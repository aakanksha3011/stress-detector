from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("stress_model.pkl")

QUESTIONS = [
    "Did you feel mentally tired today?",
    "Was it hard to focus?",
    "Did you feel overwhelmed?",
    "Did small things irritate you?",
    "Did you feel emotionally drained?",
    "Did you struggle to relax?"
]

@app.route("/")
def home():
    return "AI Stress Backend Running"

@app.route("/questions")
def questions():
    return jsonify(QUESTIONS)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    # answers = [0,1,2,1,2,1]
    answers = data["answers"]

    # emotion_score from face (0-2)
    emotion = data.get("emotion", 1)

    features = [
        answers[0],
        answers[1],
        answers[2],
        emotion
    ]

    prediction = model.predict([features])[0]

    advice = {
        "Low": "You are doing well. Maintain balance.",
        "Moderate": "Take short breaks and reduce overload.",
        "High": "High stress detected. Rest and seek support."
    }

    return jsonify({
        "stress_level": prediction,
        "advice": advice[prediction],
        "features_used": features
    })

if __name__ == "__main__":
    app.run(debug=True)
