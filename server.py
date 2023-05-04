from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app, origins=["*"], methods=["GET", "POST"])

@app.route('/status', methods=['GET'])
def main():
    retorno = {
        "status_api": "api online!"
    }
    return jsonify(retorno), 200

if __name__ == "__main__":
    app.run(host = 'localhost', port = 9000, debug = True)
