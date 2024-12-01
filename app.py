from transformers import pipeline
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

pipe = pipeline('text2text-generation', model='google/flan-t5-base')

@app.route('/ai', methods=['POST'])
def ai():
    if 'text' not in request.get_json() or 'prompt' not in request.get_json():
        return jsonify({'error': 'data missing'}), 400
    text = request.get_json()['text']
    prompt = request.get_json()['prompt']
    reply = pipe('Text: '+text+'. Prompt: '+prompt, max_length=512, do_sample=False)[0]['generated_text']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)