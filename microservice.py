from collections import Counter
import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/count_words', methods=['POST'])
def count_words():
    data = request.get_json()
    url = data['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    words = soup.get_text().split()
    word_counts = Counter(words)
    result = [{'word': word, 'count': count} for word, count in word_counts.items()]
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
