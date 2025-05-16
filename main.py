
import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    consulta = data.get('consulta', '')

    prompt = f"""
    Eres un asistente jurídico experto en el Código Penal español. Analiza los siguientes hechos y proporciona:
    1. El artículo del Código Penal aplicable.
    2. Una explicación clara y técnica del artículo.
    3. Un ejemplo práctico que ayude al usuario a entender la aplicación.

    Hechos: {consulta}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente jurídico experto en el Código Penal español."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=1000
        )
        resultado = response.choices[0].message.content
        return jsonify({"respuesta": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return "<!-- Desarrollado por Bassy Bololo Riokaló (Crimval) | JuriGPT Penal 2025 -->", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
