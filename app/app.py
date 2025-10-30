from flask import Flask, render_template, request, jsonify
import json
import random
import os

app = Flask(__name__, template_folder="templates")

# Load fixed responses
RESPONSES_FILE = os.path.join(os.path.dirname(__file__), "responses.json")
with open(RESPONSES_FILE, "r", encoding="utf-8") as f:
    RESPONSES = json.load(f)  # expected to be a list or dict

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    msg = (data.get("message") or "").strip().lower()

    # Very simple matching: if a keyword in message -> respond; otherwise random fallback
    for entry in RESPONSES:
        keywords = entry.get("keywords", [])
        for kw in keywords:
            if kw.lower() in msg:
                return jsonify({"reply": entry["reply"]})

    # fallback: return random canned message
    fallback = [e["reply"] for e in RESPONSES if e.get("fallback")]
    if fallback:
        return jsonify({"reply": random.choice(fallback)})
    else:
        return jsonify({"reply": "Sorry, I don't understand. Try asking something else."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
