from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pathlib import Path

from pathlib import Path


load_dotenv(Path(__file__).resolve().parent.parent / ".env")

print("MONGO_URI =", os.getenv("MONGO_URI"))
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

print("Mongo URI:", mongo_uri)

if not mongo_uri:
    raise Exception("MONGO_URI is missing")

client = MongoClient(mongo_uri)

db = client["The Style Algorithm"]

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
