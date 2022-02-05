from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    variavel = "Game: Adivinhe o número correto"
    if request.method == "GET":
        return render_template("index.html",variavel=variavel)
    else:
        numero = 0
        palpite = int(request.form.get("name"))
        if numero == palpite:
            return '<h1>Resultado: Você Ganhou</h1>'
        else:
            return '<h1>Resultado: Você Perdeu</h1>'

@app.route('/sobre')
def sobre():
    return 'Sobre'


@app.route('/<string:nome>')
def error(nome):
    variavel = f'Pagina ({nome} não existe)'
    return render_template('error.html',variavel=variavel)

# Para compiliar
# Primeiro você deve exportar
# export FLASK_APP=index.py (Linux, Mac)
# set FLASK_APP=index.py (windows)
# flask run

#Para que todas a alteração seja atualizadas
#o modo debug mode deve está ativado
#export FLASK_ENV=development
#set FLASK_ENV_development (windows)
#flask run