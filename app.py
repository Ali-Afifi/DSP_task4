from flask import Flask, request, send_file
from flask_cors import CORS
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
import os
import base64
from combine import *
import json

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

CORS(app)


@app.route("/", methods=["GET", "POST"])
def main():
    return send_file("./static/html/index.html")


@app.route("/saveImg", methods=["POST", "GET"])
def save_Img():
    if request.method == "POST":
        list_img = os.listdir("output")
        for img in list_img:
            path = "./output/" + img
            os.remove(path)
        img_1_edges = ((int(float(request.form["img1_y1"])), int(float(request.form["img1_y2"]))), (int(
            float(request.form["img1_x1"])), int(float(request.form["img1_x2"]))))
        img_2_edges = ((int(float(request.form["img2_y1"])), int(float(request.form["img2_y2"]))), (int(
            float(request.form["img2_x1"])), int(float(request.form["img2_x2"]))))
        option = request.form["option"]
        original_1 = base64.b64decode(request.form["original_1"].split(',')[1])
        original_2 = base64.b64decode(request.form["original_2"].split(',')[1])

        filename3 = './input/original1.png'
        filename4 = './input/original2.png'
        with open(filename3, 'wb') as f:
            f.write(original_1)
        with open(filename4, 'wb') as f:
            f.write(original_2)
        image_1 = get_combined(option, img_1_edges, img_2_edges,
                               request.form["checkbox"], request.form["checkbox_Magnitude"])
    return json.dumps({1: f'<img src="{image_1}"  id="comb_img" alt="" >'})


@app.route("/output/<image_name>", methods=["GET"])
def send_images(image_name):
    return send_file(f"./output/{image_name}", mimetype="image/png")


@app.route("/test", methods=["POST"])
def save_image():
    # data = json.loads(request.get_json())
    data = request.get_json()


    with open("./test/img1.png", 'wb') as f:
        f.write(base64.b64decode(data["image1"].split(",")[1]))
    with open("./test/img2.png", 'wb') as f:
        f.write(base64.b64decode(data["image2"].split(",")[1]))

    return "done"


if __name__ == "__main__":
    app.run(debug=True)
