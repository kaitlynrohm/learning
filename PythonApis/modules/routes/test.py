from flask import Blueprint, jsonify
from controller.my_module import greetings

test_bp = Blueprint("test", __name__)
@test_bp.route("/test1", methods=["GET"])
def test1():
    message = greetings("Sav")
    return jsonify({"greeting": message})

@test_bp.route("/test2", methods=["GET"])
def test2():
    return jsonify({"test": "TWO"})