from flask import Flask, request
from forms import LoginForm
from flask_bcrypt import Bcrypt

app = Flask(__name__)
""" Passando as configurações condidas no arquivo config """
app.config.from_pyfile('config.py')
""" instânciando a biblioteca bcrypt """
bcrypt = Bcrypt(app)
    
""" rota com metodo http post """
@app.route('/login', methods=["POST"])
def login():
    
    """ Instanciando a classe form """
    form = LoginForm()
    """ validando as informações do formulario quando é enviado """
    if form.validate_on_submit():
        """ validando se é o admin """
        if form.validate_admin(form):
            return "Acesso Concedido"
        return "Acesso negado"

if __name__ == "__main__":
    app.run(debug=True)