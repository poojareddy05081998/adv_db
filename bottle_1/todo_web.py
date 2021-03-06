
import sqlite3
import os
from bottle import get,post,template,request,redirect,debug

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ.keys()

assert ON_PYTHONANYWHERE == False

if ON_PYTHONANYWHERE:
    pass
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

# debug(True)
# run (host='localhost',port=8080)
if ON_PYTHONANYWHERE:
    pass
else:
    debug(True)
    run(host="localhost", port=8080)
