# SkSys Api Aufgabe 2

## Api Endpoints

### /api/todo

#### Post

Erwartet ein json Objekt mit {"deadline": "<date>", "description": "<desc>", "percent_done": <pd>}.

Wobei <date> ein Datum als String im Format yyyy-mm-dd ist, <desc> ein String mit unter 100 chars ist und <pd> eine Zahl zwischen 0 und 100.

#### GET

Alle Todos in eine json objekt wie oben beschrieben.


### /api/todo/<todo_id>

#### DELETE

löscht das entsprechende Todo.

#### POST

Updatet die im json übergebenen Werte im entsprechenden Todo.
