from flask import Flask,request, redirect, url_for,render_template
import pymysql
import dbf

db = pymysql.connect(user='root', password='root', database='tasks', host='localhost')

app = Flask(__name__)

@app.route('/index')
def index():
    tasks=dbf.show_tasks(db)
    return render_template('index.html',tasks=tasks)

@app.route('/newtask', methods=['POST'])
def newtask():
    newtask = request.form['newtask']
    dbf.new_task(db,newtask)
    return redirect(url_for('index'))

@app.route('/removetask<task>' )
def removetask(task):
    dbf.remove_task(db,task)
    return redirect(url_for('index'))


@app.route('/')
def hello_world():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
