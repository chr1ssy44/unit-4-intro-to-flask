from flask import Flask, render_template, request

app = Flask(__name__)

todos = ['get my nails done','spend time with my family']

@app.route('/', methods =['GET','POST'])
def index():
    new_todo = request.form["new_todo"]
    todos.append(new_todo)
    return render_template('todo.html.jinja', my_todos=todos)

