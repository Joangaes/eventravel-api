from flask import Blueprint, render_template, abort,Response,request, redirect
import pymongo
import requests
from pymongo import MongoClient
from bson import json_util, ObjectId
import json
from .validators.event_validator import EventValidator
spotify_blueprint = Blueprint('spotify_blueprint', __name__,
                        template_folder='templates')

redirect_uri = 'http://localhost:5000/spotify/login_callback'

@spotify_blueprint.route('/login')
def spotify_login():
    scopes = 'user-read-private user-read-email user-read-recently-played user-top-read';
    url = 'https://accounts.spotify.com/authorize' + '?response_type=code' + '&client_id=' + 'a0fcf6650c6345aea70db242c755b761' +  '&redirect_uri='+ redirect_uri + '&scope=' + scopes
    return redirect(url)

@spotify_blueprint.route('/login_callback')
def spotify_callback():
    code = request.args['code']
    r = requests.post('https://accounts.spotify.com/api/token',
    data={"grant_type":'authorization_code','code':code,
    'redirect_uri':redirect_uri,'client_id':'a0fcf6650c6345aea70db242c755b761','client_secret':"561d550f76fc439c92af8608dc547de7"})
    response_dict = json.loads(r.text)
    access_token = response_dict['access_token']
    refresh_token = response_dict['refresh_token']
    r = requests.get("https://api.spotify.com/v1/me/top/artists",headers={"Authorization":"Bearer " + access_token})
    print('Got response')
    print(r.status_code)
    print(r.text)
    return r.text
    