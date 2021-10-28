from flask import Flask, send_file, jsonify
from flask_cors import CORS

from service import *
from config import *

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/')
def index():
    return 'This is a programming challenge'

@app.route('/api/v1/generatefile/')
def generatefile():
    try:
        filename = generate_file()
        url = baseUrl + '/api/v1/getfile/'
        data = {'downloadurl': url, 'filename': filename}
        return jsonify(data), 200
    except:
        return 404

@app.route('/api/v1/getfile/')
def getfile():
    try:
        return send_file(fileName, as_attachment="True"), 200
    except:
        return 404

@app.route('/api/v1/objectcount/')
def objectcount():
    try:
        result = get_object_count()
        return jsonify(result), 200
    except:
        return 404


if __name__ == '__main__':
    app.run()
