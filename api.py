'''
backend client-server interactions
'''

import flask

app = flask.Blueprint("api_app", __name__)

@app.route("/ping")
def ping():
    return "Hello World!"

@app.route("/api/convo")
def convo():
    return ""

@app.route("/api/user")
def user():
    return ""