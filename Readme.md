# ToDo API

This is an example ToDo API made in flask, using SQLite as database for data persistence

## Installation guide

1. Clone this repo
1. Create a python virtual environment and open it
1. Install requirements: `pip install -r requirements.txt`
1. Run the project: `python api.py`

## API Spec

### `/`

Sanity check, to know if everything is working properly

### `/todos`

#### `GET`

Get all ToDos

#### `POST`

Create a new ToDo, sending content in JSON format

Example:

```json
{ "content": "Hello World!" }
```

### `/todos/<int:id>`

#### `GET`

Get one ToDo by id.

#### `PUT`

Update one ToDo by id, sending new content in JSON format

Example:

```json
{ "content": "Hello World!" }
```

#### `DELETE`

Delete one ToDo by id.
