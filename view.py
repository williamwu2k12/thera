'''
frontend view rendering
'''

import flask

app = flask.Blueprint("view_app", __name__)

@app.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return flask.render_template("about.html")

@app.route("/chat", methods=["GET"])
def chat():
    return flask.render_template("chat.html")

@app.route("/user", methods=["GET"])
def user():
    return flask.render_template("user.html")