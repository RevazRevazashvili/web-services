from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app, resources={r"/calculator/*": {"origins": "http://127.0.0.1:5500"}})


@app.route("/todolist/registration", methods=["GET"])
def registration():
    name_patt = re.compile(r"[a-z A-Z]+")
    pattern = r"password: ([\d,]+)"
    user_name = request.args.get("username")
    password = request.args.get("password")

    if name_patt.findall(user_name) and password:
        with open("users.txt", 'r') as f:
            for line in f:
                stored_username, stored_password = map(str.strip, line.split(' '))

                if stored_password == password:
                    return jsonify(f"error: password already exists")
                
        with open("users.txt", 'a') as file:
            file.write(f"{user_name} {password}")
        return jsonify("successfully registered")
    else:
        return jsonify(f"error: invalid username or password")


if __name__ == "__main__":
    app.run(debug=True)
