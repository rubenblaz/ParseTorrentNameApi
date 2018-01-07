"""
Parse Torrent Name API

Provides an API for parsing torrent names as a micro-service, primarily for use
with other programming languages that do not have the same library.
"""
from flask import Flask, jsonify, request
import PTN

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():
    """
    Endpoint for parsing a list of torrent names for scene information

    Receives a list of strings and returns objects containing the scene information
    For more information on the name parsing see https://github.com/divijbindlish/parse-torrent-name
    """
    filenames = request.get_json()

    pretty_names = {}

    for filename in filenames:
        pretty_names[filename] = PTN.parse(filename)

    return jsonify(pretty_names)

if __name__ == '__main__':
    app.run()