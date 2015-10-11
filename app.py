import json

import flask
import view
import api

app = flask.Flask(__name__)
app.register_blueprint(api.app)
app.register_blueprint(view.app)
app.debug = True

if __name__ == "__main__":
    app.run()
