from flask import Flask, request, jsonify


app = Flask(__name__)


""" Rota com metodo Http Get """
@app.route("/saudacao", methods=["GET"])
def getNome():
    """ Pegando o valor inserido na url da rota com request """
    nome = request.args.get("nome")
    """ retornando o nome instânciado com json com jsonify """
    return jsonify({"message": f"saudação {nome}"})

""" Rota com metodo Http Post """
@app.route("/soma", methods=["POST"])
def postSoma():
    """ recebendo os valores enviados via post """
    number = request.get_json()
    
    """ pegando os valores pelas chaves do json e instânciando para uma nova variavel e somando """
    n1 = number.get("n1")
    n2 = number.get("n2")
    soma = n1 + n2
    """ retornando a soma dos valores com json"""
    return jsonify({"message": f"{soma}"})


if __name__ == "__main__":
    app.run(debug=True)
    
    
