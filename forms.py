from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
from app import bcrypt
import os

""" usando a biblioteca dotenv para esconder em um arquivo .env a senha encriptada do admin """
HASH_ADMIN = os.getenv("HASH_ADMIN")

""" o flaskForm gera tokens aleatorios e é adicionado ao formulario assim protegendo de ataques csrf """
class LoginForm(FlaskForm):
    usuario = StringField(label='Usuario', validators=[DataRequired()])
    senha = PasswordField(label='Senha', validators=[DataRequired()])
    
    """ função que verifica se o login é de um admin, sem necessidade de fazer a validação na rota """
    def validate_admin(self, form):
        
        """ Verificando se o hash_admin esta definido """
        if not HASH_ADMIN:
            raise ValueError("HASH_ADMIN não foi definida")
        
        """ Verificando se as informações são verdadeiras e se é o admin """
        """ usando a bilioteca do flask bcrypt, para checar se a senha que foi encriptada é a senha do admin """
        if form.usuario.data == 'admin' and bcrypt.check_password_hash(HASH_ADMIN, form.senha.data):
            return True
        return False