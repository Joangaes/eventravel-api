from flask import Blueprint, render_template, abort,Response,request
import pymongo
from pymongo import MongoClient
from bson import json_util, ObjectId
import json
from .validators.event_validator import EventValidator
event_blueprint = Blueprint('event_blueprint', __name__,
                        template_folder='templates')

def get_db():
    client = MongoClient(host='localhost',
                         port=27017, 
                         username='joangaes', 
                         password='password',
                        authSource="admin")
    db = client["eventravel"]
    return db


@event_blueprint.route('/')
def ping_server():
    return "Welcome to the world of events."

@event_blueprint.route('/',methods=["POST"])
def saveEvent():
    data = request.json
    #if not EventValidator().validate(data):
    #    return Response(response=json.dumps({"Error": "Please provide correct data"}),
    #                    status=400,
    #                    mimetype='application/json')
    try:
        db = get_db()
        db.eventravel.insert_one(data)
        data = json.loads(json_util.dumps(data))
        return Response(response=json.dumps(data),
                    status=200,
                    mimetype='application/json')
    except Exception as err:
        print(err)
        return Response(response=str({'message': 'Could not save the data'}),status=400)
    