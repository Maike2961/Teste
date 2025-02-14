from flask import Flask, request
from forms import LoginForm
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')
bcrypt = Bcrypt(app)
    

@app.route('/login', methods=["POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.validate_admin(form):
            return "Acesso Concedido"
        return "Acesso negado"

if __name__ == "__main__":
    app.run(debug=True)