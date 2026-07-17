from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pathlib import Path

from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

print("MONGO_URI =", os.getenv("MONGO_URI"))
client = MongoClient(os.getenv("MONGO_URI"))
db = client["avora"]
users = db["users"]

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():

    data = request.json

    # Check if email already exists
    existing = users.find_one({"email": data["email"]})

    if existing:
        return jsonify({"message": "Email already exists"}), 400

    users.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    })

    return jsonify({
        "message": "Registration Successful"
    }), 201