from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return "WeHelp AI Server Running Successfully"

@app.route("/test")
def test():
    return "AI Test Successful"

@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['image']

    npimg = np.frombuffer(file.read(), np.uint8)

    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur Detection
    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Blur image
    if blur_score < 30:
        return jsonify({
            "status": "Invalid Image",
            "score": 0
        })

    # Brightness Analysis
    brightness = np.mean(gray)

    if brightness > 120:
        status = "Fresh"
        score = 85
    else:
        status = "Possibly Expired"
        score = 45

    return jsonify({
        "status": status,
        "score": score
    })

if __name__ == "__main__":
    app.run()
