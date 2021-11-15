from flask import Flask, jsonify,request,Response
import pymongo
from pymongo import MongoClient
from blueprints.event_blueprint import event_blueprint
from blueprints.spotify_blueprint import spotify_blueprint
app = Flask(__name__)
app.register_blueprint(event_blueprint, url_prefix='/event')
app.register_blueprint(spotify_blueprint,url_prefix='/spotify')


def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["eventravel"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the world of animals."



@app.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _animals = db.eventravel.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
