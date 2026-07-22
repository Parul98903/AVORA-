from flask import Blueprint, request, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
print("MONGO_URI =", os.getenv("MONGO_URI"))

client = MongoClient(os.getenv("MONGO_URI"))
db = client["the_style_algorithm"]
wardrobe_collection = db["wardrobe"]

wardrobe = Blueprint("wardrobe", __name__)
uploaded_clothes = []

@wardrobe.route("/wardrobe")
def wardrobe_page():
    return render_template("wardrobe.html")


@wardrobe.route("/wardrobe/add", methods=["POST"])
def add_clothing():

    image = request.files.get("image")

    if image is None:
        return jsonify({"message": "No image selected"}), 400

    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    filename = image.filename
    image.save(os.path.join(upload_folder, filename))

    item = {
        "user_email": "parul@gmail.com",
        "category": request.form.get("category"),
        "color": request.form.get("color"),
        "brand": request.form.get("brand"),
        "image": filename
    }

    wardrobe_collection.insert_one(item)

    return jsonify({
        "message": "Clothing uploaded successfully!"
    }), 200
@wardrobe.route("/wardrobe/items")
def get_items():
    
    return jsonify(uploaded_clothes)
    return jsonify({
        "message": "Image uploaded successfully!",
        "item": item
    }),     
    return jsonify({
        "message": "Image uploaded successfully!",
        "filename": filename,
        "category": category,
        "color": color,
        "brand": brand
    }), 200
    return jsonify({
        "message": "Image uploaded successfully!",
        "filename": filename
    }), 200
    wardrobe_collection.insert_one(item)

    return jsonify({
        "message": "Clothing uploaded successfully!"
    })
@wardrobe.route("/wardrobe/delete/<item_id>", methods=["DELETE"])
def delete_item(item_id):

    global uploaded_clothes

    uploaded_clothes = [
        item for item in uploaded_clothes
        if item["id"] != item_id
    ]

    return jsonify({
        "message": "Deleted Successfully"
    })
@wardrobe.route("/wardrobe/edit/<item_id>", methods=["PUT"])
def edit_item(item_id):

    data = request.json

    for item in uploaded_clothes:

        if item["id"] == item_id:

            item["category"] = data["category"]
            item["color"] = data["color"]
            item["brand"] = data["brand"]

            return jsonify({
                "message":"Updated Successfully"
            })

    return jsonify({
        "message":"Item Not Found"
    }),404


@wardrobe.route("/wardrobe/<user_email>")
def get_wardrobe(user_email):

    clothes = list(
        wardrobe_collection.find(
            {"user_email": user_email},
            {"_id": 0}
        )
    )

    return jsonify(clothes)