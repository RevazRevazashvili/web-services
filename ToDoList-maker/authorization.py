from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/calculator/*": {"origins": "http://127.0.0.1:5500"}})


@app.route("/todolist/authorization", methods=["GET"])
def authorisation():
    user_name = request.args.get("username")
    password = request.args.get("password")

    with open("users.txt", 'r') as f:
        for line in f:
            stored_username, stored_password = map(str.strip, line.split(' '))

            if stored_username == user_name and stored_password == password:
                return redirect(url_for('welcome'))

            else:
                return jsonify(f"username {user_name} is not registered or invalid input")

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


if __name__ == "__main__":
    app.run(debug=True)
