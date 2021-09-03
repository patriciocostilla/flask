from flask import Flask, request, jsonify
from utils.todos import fetch_all, create, fetch_one, delete, update

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])
def info():
    return {
        "method": request.method,
        "path": request.path,
        "args": request.args,
        "data": request.json,
        "form-data": request.form,
    }

@app.route("/todos", methods=["GET", "POST"])
def todos():    
    if request.method == "GET":
        return jsonify(fetch_all())
    elif request.method == "POST":
        data = request.json
        content = data["content"]
        new_todo = create(content)
        return new_todo, 201

@app.route("/todos/<int:id>", methods=["GET", "PUT", "DELETE"])
def todo(id):
    if request.method == "GET":
        # Get one ToDo
        result = fetch_one(id)
        if result == None:
            return "", 404
        return result, 200
        
    elif request.method == "PUT":
        # Update one ToDo
        data = request.json
        content = data["content"]
        result = update(id, content)
        if result == None:
            return "", 404
        return result, 200
        
    elif request.method == "DELETE":
        # Delete one ToDo
        delete(id)
        return "", 200

if __name__ == "__main__":
    app.run()