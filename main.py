from flask import Flask, request, jsonify
import os
from openai import OpenAI

client = OpenAI()
app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola Sergio! Lumi Jarvis Cloud con GPT-4o ya está activo ✨'

@app.route('/hablar', methods=['POST'])
def hablar():
    data = request.json
    texto_usuario = data.get('texto', '')

    try:
        respuesta = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": texto_usuario}]
        ).choices[0].message.content
    except Exception as e:
        respuesta = f"[Error al usar OpenAI] {str(e)}"

    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
