"""
Parse Torrent Name API

Provides an API for parsing torrent names as a micro-service, primarily for use
with other programming languages that do not have the same library.
"""
from flask import Flask, jsonify, request
#import PTN
import os
from guessit import guessit

app = Flask(__name__)    
@app.route('/parse', methods=['POST'])
def parse():
    """
    Endpoint for parsing a list of torrent names for scene information

    Receives a list of strings and returns objects containing the scene information
    For more information on the name parsing see https://github.com/divijbindlish/parse-torrent-name
    """
    filename = request.get_json()
    print(filename)
    
    #pretty_names = PTN.parse(filename)
    pretty_names = guessit(filename)
    pretty_names.pop('language', None) 
    pretty_names.pop('country', None) 
    print(pretty_names)
    #aux = pretty_names.split(', ')
    return jsonify(pretty_names)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
