# A very simple Bottle Hello World app for you to get started with...
import sqlite3
import os
from bottle import get,post,template,request,redirect,debug

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ.keys()

# assert ON_PYTHONANYWHERE == True

if ON_PYTHONANYWHERE:
    from bottle import default_app
else:
    from bottle import run,redirect

@get('/')
def get_show_list():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result)

@get("/new_item")
def get_new_item():
    return template("new_item")

@post("/new_item")
def post_new_item():
    new_item=request.forms.get("new_item").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("insert into todo(task,status)values (?,?)", (new_item,1))
    #cursor.lastrowid
    connection.commit()
    cursor.close()
    #return "the new item is[" + new_item + "]..."
    redirect("/")

@get('/delete_item/<id:int>')
def get_delete_item(id):
    print("we want to delete #" + str(id))
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("delete from todo where id=?", (id,))
    connection.commit()
    cursor.close()
    redirect('/')


@get('/update_item/<id:int>')
def get_update_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo where id=?", (id,))
    result = cursor.fetchall()
    cursor.close()
    return template("update_item", row=result[0])


@post('/update_item')
def post_update_item():
    id = int(request.forms.get("id").strip())
    updated_item = request.forms.get("updated_item").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set task=? where id=?", (updated_item, id,))
    connection.commit()
    cursor.close()
    redirect('/')
# debug(True)
# run (host='localhost',port=8080)
if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host="localhost", port=8080)
