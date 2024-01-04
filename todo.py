from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print

app = Flask(__name__)

results = ['get my nails done','spend time with my family']


@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        results.append(new_todo)

    return render_template('todo.html.jinja', my_todos=results)


@app.route('/delete_todo/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    del results[todo_index]

    return redirect('/')

conn = pymysql.connect(
    database = "cbeckford2_todos",
    user = "cbeckford2",
    password = "227248309",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor
)
cursor = conn.cursor()

cursor.execute("SELECT `description` FROM `todos`")

results = cursor.fetchall()
print(results)