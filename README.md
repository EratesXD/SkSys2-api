# SkSys Api Aufgabe 2

## Api Endpoints

### /api/todo

#### Post

Erwartet ein json Objekt mit {"deadline": "<date>", "description": "<desc>", "percent_done": <pd>}.

```
{
  "deadline": "2023-03-19",
  "description": "hallo bitte einmal auf das hier ändern",
  "percent_done": 20
}
```

Wobei <date> ein Datum als String im Format yyyy-mm-dd ist, <desc> ein String mit unter 160 chars ist und <pd> eine Zahl zwischen 0 und 100.
Es muss hierbei der Content-Type im Http Header auf application/json gesetzt werden.

#### GET

Alle Todos in eine json Objekt mit Key todos und dann einer Liste mit Daten im Format von oben.

```
{
  "todos": [
    {
      "id": 2,
      "deadline": "2023-03-19",
      "description": "hallo",
      "percent_done": 20
    },
    {
      "id": 3,
      "deadline": "2020-18-19",
      "description": "Ich bin eine Beschreibung",
      "percent_done": 10
    }
  ]
}
```


### /api/todo/<todo_id>

#### DELETE

Löscht das entsprechende Todo.

#### POST

Updatet die im json übergebenen Werte im entsprechenden Todo, es reicht eine Teilmenge und nur diese werden dann geupdatet.

```
{
  "percent_done": 30
}
```

Es muss hierbei der Content-Type im Http Header auf application/json gesetzt werden.
