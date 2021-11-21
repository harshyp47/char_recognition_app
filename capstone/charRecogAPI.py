from flask import Flask, request, jsonify
from ImageDownload import Image_Download
from recognitionfunction import recognitionfunction

app = Flask(__name__)


import time
import cv2
from matplotlib import pyplot as plt
import numpy as np

@app.route('/api',methods = ["GET"])
def recognize():

    print("Button Clicked!")
    time.sleep(30)
    Image_Download()
    print("image downloaded")
    IMAGE_PATH = 'img.jpeg'
    text = recognitionfunction(IMAGE_PATH)
    d={}
    print(text)
    d['Query'] = str(text)
    return jsonify(d)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5758)
