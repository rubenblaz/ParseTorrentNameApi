"""
Parse Torrent Name API

Provides an API for parsing torrent names as a micro-service, primarily for use
with other programming languages that do not have the same library.
"""
from flask import Flask, jsonify, request
import PTN
import os

app = Flask(__name__)    
@app.route('/parse', methods=['POST'])
def parse():
    """
    Endpoint for parsing a list of torrent names for scene information

    Receives a list of strings and returns objects containing the scene information
    For more information on the name parsing see https://github.com/divijbindlish/parse-torrent-name
    """
    filenames = request.get_json()
    filenames = PTN.parse(filenames)
    if len(filenames==1):
        pretty_names = {filename:filenames}
    else:
        pretty_names = {filename:filename for filename in filenames}

    return jsonify(pretty_names)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
