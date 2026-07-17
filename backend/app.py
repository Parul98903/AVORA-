from flask import Flask, render_template, send_from_directory

from backend.routes.auth import auth
from backend.routes.wardrobe import wardrobe
from backend.routes.ai import ai

app = Flask(__name__, template_folder="templates")

app.register_blueprint(auth)
app.register_blueprint(wardrobe)
app.register_blueprint(ai)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return "test is working"

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)

if __name__ == "__main__":
    import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )