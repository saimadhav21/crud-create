from flask import Blueprint,jsonify

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/dummy-api", methods=["GET"])
def dummy_api():
    return jsonify({"message": "Dummy API is working!"}), 200