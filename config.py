import os
from dotenv import load_dotenv

load_dotenv(override=True)

""" uma secret key é necessaria quando usamos o flask form para proteger de ataques csrf e usando o dotenv para esconder 
a secret key em um arquivo .env
"""
SECRET_KEY=os.getenv("SECRET_KEY")