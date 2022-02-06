from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/foo')
def foo():
    return 'bar'



if __name__ == '__main__':
    app.run(debug=True)