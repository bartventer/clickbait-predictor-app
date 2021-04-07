###################################################
######IMPORTING PACKAGES#######
###################################################

from flask import Flask, send_from_directory, request, jsonify, json, redirect, url_for
from machineLearning.Images import Images
from machineLearning.clickbait import ClickBaitModel
import numpy as np 
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
import string as s
import re
import os
import joblib

###################################################
######CREATING AND CONFIGURING THE FLASK APP#######
###################################################
app = Flask(__name__,static_folder='client/build',static_url_path='/')
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

###################################################
# LOADING THE TRAINED MODEL AND SCALER OBJECT
###################################################
loaded_model = joblib.load("./machineLearning/model.pkl")
loaded_scaler = joblib.load("./machineLearning/scaler.pkl")

###################################################
######CREATING SOME DEFAULT ITEMS FOR THE SITE#######
###################################################
request_history = [
    {"prediction":"“How to Achieve Results Using This One Weird Trick”", "result":"Clickbait!",
    "imgUrl":"https://images.unsplash.com/photo-1613648563132-18becf444cb8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1055&q=80"},
    {"prediction":"“You'll Never Believe This _________ “", "result":"Clickbait!",
    "imgUrl":"https://images.unsplash.com/photo-1506704810770-7e9bbab1094b?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"},
    {"prediction":"“They Didn't Know _________ . Then This Happened …”", "result":"Clickbait!",
    "imgUrl":"https://images.unsplash.com/photo-1512621387945-efb0d554f388?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"}
    ]


###################################################
###### GENERATING AN IMAGE FOR THE RESULT #######
###################################################
def setImageUrl(result):
    img = Images(result)
    imgUrl = img.generateImage()
    return imgUrl


###################################################
###### FUNCTION TO SERIALIZE JSON DATA#######
###################################################
def serializer(single_prediciton):
    return {
        'prediction':single_prediciton["prediction"],
        'result':single_prediciton["result"],
        'imgUrl': single_prediciton["imgUrl"]
    }

###################################################
###### ROUTES / API's OF THE BACKEND #######
###################################################

#DEFAULT STATIC URL LOCATED IN THE BUILD DIRECTORY
@app.route('/')
def home():
    return app.send_static_file('index.html')

#API FOR ALL ITEMS
@app.route('/api', methods=['GET'])
def index():
    return jsonify([*map(serializer, request_history)])

#API TO MAKE PREDICTION WITH TRAINED MODEL
@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        request_data = json.loads(request.data)  #convert to python dictionary
        pred_request  = request_data['title']
        pred_object = ClickBaitModel(request_data)
        pred_outcome = pred_object.predict(loaded_scaler, loaded_model)
        pred_imgUrl = setImageUrl(pred_outcome)
        request_history[:0] = [{
            "prediction":pred_request,
            "result": pred_outcome,
            "imgUrl":pred_imgUrl}]
        return jsonify({
            "statusCode": 200,
            "status": "Prediction made",
            "result": "Prediction: " + pred_outcome})
    except Exception as error:
        return jsonify({
            "statusCode": 500,
            "status": "Could not make prediction",
            "result": str(error)}) 

#API TO DELETE AN ITEM
@app.route('/api/delete', methods=['POST'])
def delete():
    try:
        request_data = json.loads(request.data)  #convert to python dictionary
        item_index=int(request_data['id_num'])
        request_history.pop(item_index)
        return jsonify({
            "statusCode": 200,
            "status": "Item deleted",
            "result": "List has been updated"})
    except Exception as error:
        return jsonify({
            "statusCode": 500,
            "status": "Could not delete item.",
            "result":str(error)}) 

###################################################
# RUN SCRIPT
###################################################
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)