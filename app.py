from flask import Flask, request
import json
import mysql.connector
from mysql.connector import errorcode

app = Flask('api')

get_todos_query = "SELECT * FROM test_todos"
delete_todos_query = "DELETE FROM test_todos where id = %s"
insert_todo_query = "INSERT INTO test_todos (deadline, description, percent_done) VALUES (%s, %s, %s)"
create_todo_table = "create table test_todos(deadline varchar(10), description varchar(100), percent_done INTEGER)"


def connect_to_db():
    try:
        cnc = mysql.connector.connect(user='web_user', password='web', host='127.0.0.1', database='todo_db')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return cnc


@app.get('/api/todo')
def list_programming_languages():
    db_cnc = connect_to_db()
    cursor = db_cnc.cursor()
    cursor.execute(get_todos_query)
    todos = cursor.fetchall()
    #TODO: parse output and fill a json object with it
    db_cnc.close()
    dump = json.dumps(todos)
    return dump


@app.post('/api/todo')
def put_new_todo():
    new_todo = request.json
    values = (new_todo['deadline'], new_todo['description'], new_todo['percent_done'])
    db_cnc = connect_to_db()
    cursor = db_cnc.cursor()
    cursor.execute(insert_todo_query, values)
    db_cnc.commit()
    db_cnc.close()
    return {"exit": "success"}


@app.delete('/api/todo/<todo_id>')
def delete_todo(todo_id):
    db_cnc = connect_to_db()
    cursor = db_cnc.cursor()
    cursor.execute(get_todos_query, (todo_id,))
    db_cnc.commit()
    db_cnc.close()
    pass


if __name__ == '__main__':
    list_programming_languages()
