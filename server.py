from flask import Flask, request, jsonify
from flask_cors import CORS
from db import insert, get
app = Flask(__name__)

CORS(app, origins=["*"], methods=["GET", "POST"])

@app.route('/status', methods=['GET'])
def main():
    retorno = {
        "status_api": "api online!"
    }
    return jsonify(retorno), 200


@app.route('/cadastro', methods=['POST'])
def cadastro():
    body = request.json
    if insert(body['nome'], body['sobrenome'], body['id']):
        return jsonify({"status":"inserido com sucesso"}), 200
    return jsonify({"status":"não inserido, erro na inserção"}), 500


@app.route('/get_cadastro/<id>', methods=['GET'])
def get_cadastro(id):
    json = get(id)

    if "erro" in json:
        return jsonify({"response":"nada encontrado"}), 404


    return jsonify(json), 200


if __name__ == "__main__":
    app.run(host = 'localhost', port = 9000, debug = True)
