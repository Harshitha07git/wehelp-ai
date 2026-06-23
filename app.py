from flask import Flask, request, jsonify
import easyocr
import os

app = Flask(__name__)

reader = easyocr.Reader(['en'])

@app.route("/")
def home():
    return "NGO Verification Server Running"

@app.route("/test")
def test():
    return "NGO Verification API Working"

@app.route("/verify_ngo", methods=["POST"])
def verify_ngo():

    file = request.files["certificate"]

    filename = file.filename

    file.save(filename)

    result = reader.readtext(filename)

    text = " ".join([r[1] for r in result])

    text = text.lower()

    keywords = [
        "registration",
        "certificate",
        "society",
        "trust",
        "ngo",
        "foundation"
    ]

    score = 0

    for word in keywords:
        if word in text:
            score += 1

    os.remove(filename)

    if score >= 2:
        return jsonify({
            "status": "Verified"
        })

    return jsonify({
        "status": "Failed"
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
