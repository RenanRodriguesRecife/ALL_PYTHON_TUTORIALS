from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return render_template("index.html")

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