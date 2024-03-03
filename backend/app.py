from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from train import train_source 

app = Flask(__name__)
CORS(app)

# Serve React static files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path == "":
        return send_from_directory('../frontend/build', 'index.html')
    else:
        if os.path.exists("../frontend/build/" + path):
            return send_from_directory('../frontend/build', path)
        else:
            return send_from_directory('../frontend/build', 'index.html')

# Your API route
@app.route('/api/similar-words', methods=['POST'])
def get_similar_words():
    # Get the input word from the request
    input_word = request.json.get('word')
    input_source = request.json.get('source')

    similar_words = train_source(input_word, input_source)

    # Return the list of simila