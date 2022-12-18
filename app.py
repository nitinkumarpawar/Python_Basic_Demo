import re
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)
regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def checkPostedData(postedData, functionName):
    if (functionName == "add"):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200


class Add(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
            "Message": ret,
            "Status code": 200
        }
        return jsonify(retMap)


class Sub(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x - y
        retMap = {
            "Message": ret,
            "Status code": 200
        }
        return jsonify(retMap)


class Div(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x / y
        retMap = {
            "Message": ret,
            "Status code": 200
        }
        return jsonify(retMap)


class Multi(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x * y
        retMap = {
            "Message": ret,
            "Status code": 200
        }
        return jsonify(retMap)


class Mod(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x % y
        retMap = {
            "Message": ret,
            "Status code": 200
        }
        return jsonify(retMap)


class Email(Resource):
    def post(email):
        postedData = request.get_json()
        email = postedData["email"]
        if re.fullmatch(regex, email):
            retMap = {
                "Message": "Valid email address",
                "Status code": 200
            }
            return jsonify(retMap)
        else:
            return "Invalid email address", 301


api.add_resource(Add, "/add")
api.add_resource(Sub, "/sub")
api.add_resource(Div, "/div")
api.add_resource(Multi, "/multi")
api.add_resource(Mod, "/mod")
api.add_resource(Email, "/email")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
