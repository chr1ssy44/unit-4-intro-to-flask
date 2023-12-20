from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello<h1>'

@app.route('/ping')
def ping():
    return '<h2>pong<h2>'

@app.route('/hello/<name>')
def hello(name):
    #return 'Hello '+ name
    return f'Hello {name}'