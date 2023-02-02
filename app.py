from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import base64
from utils import adjust_images, get_combined_v2, get_combined


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

CORS(app)


@app.route("/", methods=["GET", "POST"])
def main():
    return send_file("./static/html/index.html")



@app.route("/process", methods=["POST"])
def process_images():

    if request.method == "POST":
        data = request.get_json()

        with open("./input/img1.png", 'wb') as f:
            f.write(base64.b64decode(data["image1"].split(",")[1]))
        with open("./input/img2.png", 'wb') as f:
            f.write(base64.b64decode(data["image2"].split(",")[1]))

        adjust_images("./input/img1.png", "./input/img2.png")

        # resultImagePath = get_combined(data["option"], "./input/img1.png", "./input/img2.png",
        #                                uniform_magnitude=data["mag"], uniform_phase=data["phase"])


        resultImagePath = get_combined_v2(data["option"], "./input/img1.png", "./input/img2.png",
                                       uniform_magnitude=data["mag"], uniform_phase=data["phase"])



        binary_fc       = open(resultImagePath, 'rb').read()  
        base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')
        dataurl = f'data:image/png;base64,{base64_utf8_str}'

        return jsonify(msg="done", img=dataurl)


if __name__ == "__main__":
    app.run(debug=True)
