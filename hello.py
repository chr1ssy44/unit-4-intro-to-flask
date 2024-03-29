from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html.jinja')

@app.route('/ping')
def ping():
    return '<h2>pong<h2>'

@app.route('/hello/<name>')
def hello(name):
    #return 'Hello '+ name
    return f'Hello {name}'