from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import authorization

# initialize flask app
app = Flask(__name__)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


# create Marshmallow object
ma = Marshmallow(app)


# creating database
class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False, default=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, default=datetime.now())


def __repr__(self):
    return f"<ToDoList {self.name}>"


# create ToDoList schema

class ToDoListSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "completed", "date_created")


# create instance of schemas
# for single record
todolist_schema = ToDoListSchema(many=False)

# for many records
todolist_schemas = ToDoListSchema(many=True)


@app.route("/todolist", methods=["POST"])
def add_todo():
    # if authored():
        try:
            name = request.json["name"]
            description = request.json["description"]

            new_todo = ToDoList(name=name, description=description)
            db.session.add(new_todo)
            db.session.commit()

            return todolist_schema.jsonify(new_todo)
        except Exception as e:
            return jsonify({"Error": "Invalid Request."})
    # else:
    #     return jsonify({"Error": "Please authenticate."})


@app.route("/todolist", methods=["GET"])
def get_todos():
    todos = ToDoList.query.all()
    result_set = todolist_schemas.dump(todos)
    return jsonify(result_set)


@app.route("/todolist/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = ToDoList.query.get_or_404(int(todo_id))
    return todolist_schema.jsonify(todo)


@app.route("/todolist/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = ToDoList.query.get_or_404(int(todo_id))

    name = request.json["name"]
    description = request.json["description"]
    completed = request.json["completed"]

    todo.name = name
    todo.description = description
    todo.completed = completed

    db.session.commit()

    return todolist_schema.jsonify(todo)


@app.route("/todolist/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = ToDoList.query.get_or_404(int(todo_id))
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"success": "Todo Deleted."})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
