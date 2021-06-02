from app import api
from flask import jsonify
from app.api.models import Trip
from app.api import db
from flask.globals import request

@api.route('/', methods=['GET'])
def calculate():
    t = Trip()
    data = {
        'start': request.get_json['starttime'],
        'end': request.get_json['stoptime'],
    }

    return data
