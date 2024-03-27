"""
Criando uma api simples com o Flask
"""

from flask import Flask, jsonify, render_template

from browser import get_price_cripto


APP = Flask(__name__, static_folder='templates')


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/get-price/<criptomoeda>')
def get_price(criptomoeda: str):
    price = get_price_cripto(tag=criptomoeda)
    return jsonify(price)


if __name__ == '__main__':
    APP.run(debug=True)
