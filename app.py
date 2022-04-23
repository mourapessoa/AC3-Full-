import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html') 


@app.route('/index', methods=['POST'])
def index():
    json = request.get_json()
    nome = json['nome']
    email = json['email']
    return jsonify(nome=nome, email=email)


if __name__ == "__main__":
    app.run(debug=True)


