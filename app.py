
from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return "Lumi Jarvis Cloud está activa."

@app.route("/lumi", methods=["POST"])
def lumi():
    data = request.json
    texto = data.get("mensaje", "")
    if not texto:
        return jsonify({"error": "Mensaje vacío"}), 400

    respuesta = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": texto}]
    )
    return jsonify({"respuesta": respuesta.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
