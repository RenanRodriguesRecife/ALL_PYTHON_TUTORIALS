from flask import Flask
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'Ola Mundo'


# Para compiliar
# Primeiro você deve exportar
# export FLASK_APP=index.py (Linux, Mac)
# set FLASK_APP=index.py (windows)
# flask run