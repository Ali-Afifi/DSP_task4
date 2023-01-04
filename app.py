from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import base64
from utils import adjust_images, get_combined


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

CORS(app)


@app.route("/", methods=["GET", "POST"])
def main():
    return send_file("./static/html/index.html")


@app.route("/output/<image_name>", methods=["GET"])
def send_images(image_name):
    return send_file(f"./output/{image_name}", mimetype="image/png")


@app.route("/test", methods=["POST"])
def process_images():

    if request.method == "POST":
        data = request.get_json()

        with open("./input/img1.png", 'wb') as f:
            f.write(base64.b64decode(data["image1"].split(",")[1]))
        with open("./input/img2.png", 'wb') as f:
            f.write(base64.b64decode(data["image2"].split(",")[1]))

        adjust_images("./input/img1.png", "./input/img2.png")

        resultImagePath = get_combined(data["option"], "./input/img1.png", "./input/img2.png",
                                       uniform_magnitude=data["mag"], uniform_phase=data["phase"])

        return jsonify(msg="done", img=resultImagePath)


if __name__ == "__main__":
    app.run(debug=True)
