from flask import Blueprint, jsonify

test_bp = Blueprint("test", __name__)
@test_bp.route("/test1", methods=["GET"])
def test1():
    return jsonify({"test": "ONE"})

@test_bp.route("/test2", methods=["GET"])
def test2():
    return jsonify({"test": "TWO"})