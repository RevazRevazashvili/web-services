#############  RESTapi  ################

##  calculator  ##

from flask import Flask,jsonify,request
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app, resources={r"/calculator/*": {"origins": "http://127.0.0.1:5500"}})

# defineing add function
@app.route('/calculator/add', methods=["GET"])
def add():
    user_data = {
        "sum": ""
    }
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    
    user_data["sum"] = num1+num2
    return jsonify(user_data), 200

# defineing subtract function
@app.route('/calculator/subtract', methods=["GET"])
def subtract():
    user_data = {
        "sum": ""
    }
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    
    user_data["sum"] = num1-num2
    return jsonify(user_data), 200


# defineing multiply function
@app.route('/calculator/multiply', methods=["GET"])
def multiply():
    user_data = {
        "sum": 10
    }
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    
    user_data["sum"] = num1*num2
    return jsonify(user_data), 200


# defineing divide function
@app.route('/calculator/divide', methods=["GET"])
def divide():
    user_data = {
        "result": ""
    }

    try:
        num1 = int(request.args.get("num1"))
        num2 = int(request.args.get("num2"))

        if num2 == 0:
            raise ValueError("Division by zero is not allowed")

        user_data["result"] = num1 / num2
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# defineing sqrt function
@app.route('/calculator/sqrt', methods=["GET"])
def squareroot():
    user_data = {
        "sum": 10
    }
    num1 = int(request.args.get("num1"))
    
    user_data["sum"] = math.sqrt(num1)
    return jsonify(user_data), 200


# defineing modulus function
@app.route('/calculator/modulus', methods=["GET"])
def modulus():
    user_data = {
        "sum": 10
    }
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    
    user_data["sum"] = num1%num2
    return jsonify(user_data), 200


# defineing mod function
@app.route('/calculator/mod', methods=["GET"])
def mod():
    user_data = {
        "sum": 10
    }
    num1 = int(request.args.get("num1"))
    if num1<0:
        user_data["sum"] = num1*(-1)
    else:
        user_data["sum"] = num1
    return jsonify(user_data), 200


@app.route('/calculator/power', methods=["GET"])
def power():
    user_data = {
        "sum": ""
    }
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    
    user_data["sum"] = num1**num2
    return jsonify(user_data), 200

if __name__=="__main__":
    app.run(debug=True)