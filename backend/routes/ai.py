from flask import Blueprint, request, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[""]
wardrobe = db["wardrobe"]

ai = Blueprint("ai", __name__)

# ---------------- AI PAGE ----------------

@ai.route("/ai")
def ai_page():
    return render_template("ai.html")


# ---------------- GENERATE OUTFIT ----------------

@ai.route("/generate-outfit", methods=["POST"])
def generate_outfit():

    data = request.json

    print("Received:", data)

    user_email = data["user_email"]
    occasion = data["occasion"]

    clothes = list(
        wardrobe.find(
            {"user_email": user_email},
            {"_id": 0}
        )
    )

    print("Clothes:", clothes)

    tops = [x for x in clothes if x["category"] == "Top"]
    bottoms = [x for x in clothes if x["category"] == "Bottom"]
    dresses = [x for x in clothes if x["category"] == "Dress"]
    shoes = [x for x in clothes if x["category"] == "Shoes"]

    outfit = {}

    if occasion == "Party":

        if dresses:
            outfit["Dress"] = dresses[0]

        elif tops and bottoms:
            outfit["Top"] = tops[0]
            outfit["Bottom"] = bottoms[0]

        if shoes:
            outfit["Shoes"] = shoes[0]

    elif occasion == "Office":

        if tops:
            outfit["Top"] = tops[0]

        if bottoms:
            outfit["Bottom"] = bottoms[0]

        if shoes:
            outfit["Shoes"] = shoes[0]

    else:

        if tops:
            outfit["Top"] = tops[0]

        if bottoms:
            outfit["Bottom"] = bottoms[0]

        if shoes:
            outfit["Shoes"] = shoes[0]

    print("Outfit:", outfit)

    return jsonify(outfit)