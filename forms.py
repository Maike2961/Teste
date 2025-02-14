from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
from app import bcrypt
import os

HASH_ADMIN = os.getenv("HASH_ADMIN")

class LoginForm(FlaskForm):
    usuario = StringField(label='Usuario', validators=[DataRequired()])
    senha = PasswordField(label='Senha', validators=[DataRequired()])
    
    def validate_admin(self, form):
        
        if not HASH_ADMIN:
            raise ValueError("HASH_ADMIN não foi definida")
        
        if form.usuario.data == 'admin' and bcrypt.check_password_hash(HASH_ADMIN, form.senha.data):
            return True
        return False