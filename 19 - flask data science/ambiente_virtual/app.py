from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/foo')
def foo():
    return 'bar'

@app.route('/hi/<name>')
def hi(name):
    return f'Hi {name}!'

@app.route('/api')
def api():
    data = {
        'name': 'Andrew',
        'user': 'acroz'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)



# O Python tem suporte a JSON em sua biblioteca padrão, 
# mas ao usar o Flask recomendamos o uso do  jsonify()auxiliar, 
# que não apenas serializa seus dados para JSON, mas também
#  prepara um Response objeto Flask com coisas úteis como a
#   predefinição do tipo de conteúdo HTTP.

# flask.jsonify(), não funciona bem com os tipos NumPy
# voce deve converter para numeros nativos python

# numpy_integer = numpy.int64(3)
# json.dumps(int(numpy_integer))
# para array
# array_1d = numpy.array([1., 1.5, 2.])
# json.dumps([float(v) for v in array_1d])
# '[1.0, 1.5, 2.0]'
# array_2d = numpy.array([[1., 1.5], [1.5, 2.]])
# json.dumps([[float(v) for v in row] for row in array_2d])
# '[[1.0, 1.5], [1.5, 2.0]]'