from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/saudacao", methods=["GET"])
def getNome():
    nome = request.args.get("nome")
    return jsonify({"message": f"saudação {nome}"})

@app.route("/soma", methods=["POST"])
def postSoma():
    number = request.get_json()
    
    n1 = number.get("n1")
    n2 = number.get("n2")
    soma = n1 + n2
    return jsonify({"message": f"{soma}"})


if __name__ == "__main__":
    app.run(debug=True)
    
    
