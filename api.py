'''
backend client-server interactions
'''

import flask
import sqlite3
import firebase
import hashlib

app = flask.Blueprint("api_app", __name__)

database_url = "https://thera.firebaseio.com"
database = firebase.firebase.FirebaseApplication(database_url, None)
# authenticate so only user can see

@app.route("/ping", methods=["GET"])
def ping():
    return "Hello World!"

@app.route("/api/convo", methods=["GET"])
def convo():
    return ""

@app.route("/api/user", methods=["GET"])
def user():
    return ""

@app.route("/api/login")
def login():
    username = flask.request.args.get("username")
    password = flask.request.args.get("password")
    result = database.post_async("/users", {username: hashlib.sha256(password).hexdigest()})
    return "Username Password Successfully Setup!"
