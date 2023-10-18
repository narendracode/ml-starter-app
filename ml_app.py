import flask
import io
import string
import time
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, jsonify, request
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import json

model = tf.keras.models.load_model('model.h5')

class animal:
    def __init__(self, name, prediction):
        self.name = name
        self.prediction = prediction

def prepare_image(img):
    img = Image.open(io.BytesIO(img))
    img = img.resize((224, 224))
    img = np.array(img)
    img = np.expand_dims(img, 0)
    return img


def predict_result(img):
    preds = model.predict(img)
    decoded_preds = decode_predictions(preds, top=3)[0]
   
    #storing the result
    species = []
    for p in decoded_preds:
        species.append({"name": p[1], "prediction": str(p[2])})
    return species

app = Flask(__name__)

@app.route("/")
def index_page():
    return "<p>Index Page</p>"


@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return "Please try again. The Image doesn't exist"
    
    file = request.files.get('file')

    if not file:
        return

    img_bytes = file.read()
    img = prepare_image(img_bytes)

    return jsonify(predict_result(img))
