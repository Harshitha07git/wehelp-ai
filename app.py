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

if __name__ == "__main__":
    app.run()
