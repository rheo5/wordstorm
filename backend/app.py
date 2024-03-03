from flask import Flask, request, jsonify
from flask_cors import CORS
from train import train_source 

app = Flask(__name__)
CORS(app)

# Route to handle requests for similar words
@app.route('/api/similar-words', methods=['POST'])
def get_similar_words():
    # Get the input word from the request
    input_word = request.json.get('word')
    input_source = request.json.get('source')

    similar_words = train_source(input_word, input_source)

    # Return the list of similar words as JSON response
    return jsonify(similarWords=similar_words)  

if __name__ == '__main__':
    app.run(debug=True)
