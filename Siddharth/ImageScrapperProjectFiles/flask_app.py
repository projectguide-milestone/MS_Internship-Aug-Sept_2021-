# Importing the necessary Libraries
from flask_cors import CORS,cross_origin
from imagescrapperservice.ImageScrapperService import ImageScrapperService
from imagescrapper.ImageScrapper import ImageScrapper
from flask import Flask, render_template, request,jsonify


# import request
app = Flask(__name__) # initialising the flask app with the name 'app'

#response = 'Welcome!'


@app.route('/')  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')


