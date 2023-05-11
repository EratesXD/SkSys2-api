from flask import Flask, request
import json
import mysql.connector
from mysql.connector import errorcode

app = Flask('api')

get_todos_query = "SELECT * FROM test_todos"

delete_todos_query = "DELETE FROM test_todos where id = %s"

insert_todo_query = "INSERT INTO test_todos (deadline, description, percent_done) VALUES (%s, %s, %s)"

update_desc_query= "UPDATE test_todos " \
                   "SET description = %s " \
                   "WHERE id = %s"
update_pd_query= "UPDATE test_todos " \
                   "SET percent_done = %s " \
                   "WHERE id = %s"
update_date_query= "UPDATE test_todos " \
                   "SET deadline = %s " \
                   "WHERE id = %s"

create_todo_table = "CREATE TABLE IF NOT EXISTS test_todos(" \
                    "id MEDIUMINT NOT NULL AUTO_INCREMENT, " \
                    "deadline VARCHAR(10) NOT NULL , " \
                    "description VARCHAR(160) NOT NULL , " \
                    "percent_done INTEGER NOT NULL," \
                    "PRIMARY KEY (id))"


def connect_to_db():
    try:
        cnc = mysql.connector.connect(user='web_user', password='supersecureweb', host='192.168.178.85', database='todo_db')
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
    todos_list = cursor.fetchall()
    db_cnc.close()
    todos = []
    for id, dl, desc, pd in todos_list:
        todos.append(dict(id = id, deadline = dl, description = desc, percent_done = pd))
    todos_json = json.dumps(dict(todos = todos))
    return todos_json


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


@app.post('/api/todo/<todo_id>')
def update_todo(todo_id):
    vals_to_update = request.json
    db_cnc = connect_to_db()
    cursor = db_cnc.cursor()

    if 'description' in vals_to_update:
        cursor.execute(update_desc_query, (vals_to_update['description'], todo_id))
    if 'percent_done' in vals_to_update:
        cursor.execute(update_pd_query, (vals_to_update['percent_done'], todo_id))
    if 'deadline' in vals_to_update:
        cursor.execute(update_date_query, (vals_to_update['deadline'], todo_id))

    db_cnc.commit()
    db_cnc.close()
    return {"exit": "success"}


@app.delete('/api/todo/<todo_id>')
def delete_todo(todo_id):
    db_cnc = connect_to_db()
    cursor = db_cnc.cursor()
    cursor.execute(delete_todos_query, (todo_id,))
    db_cnc.commit()
    db_cnc.close()
    return {"exit": "success"}


if __name__ == '__main__':
    db_cnc = connect_to_db()
    cursor = db_cnc.cursor()
    cursor.execute(create_todo_table)
    db_cnc.commit()
    db_cnc.close()
    print(list_programming_languages())
