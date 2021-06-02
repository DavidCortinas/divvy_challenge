from app.api import app
from flask import jsonify
from app.api.models import Trip
from app.api import db
from flask.globals import request
from datetime import datetime

@app.route('/', methods=['GET'])
def instructions():
    # data = {
    #     "This": "Works"
    # }

    data = "Navigate to '.../calculate' and add the following query parameters: start (i.e. '2013-06-28'), end (i.e. '2013-06-30')"

    return data

@app.route('/calculate?start=<starttime>&&end=<stoptime>', methods=['GET'])
def calculate(starttime, stoptime):


    data = {
        "averageDuration": stoptime-starttime
    }

    return data
