from flask import Flask, send_file, jsonify
from flask_cors import CORS

from service import *

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/api/v1/getfile/')
def gettextfile():
    try:
        filename = generate_file()
        # filename ='Badruzzaman.pdf'
        return send_file(filename), 200
    except:
        print('something went wrong')

@app.route('/api/v1/objectcount/')
def objectcount():
    try:
        result = get_object_count()
        return jsonify(result), 200
    except:
        print('something went wrong')


if __name__ == '__main__':
    app.run()
