import os
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, url_for

from controller.compte import compte
from model_db.shared_model import db


app = Flask(__name__, template_folder="view")
app.config.from_object("config.DevConfig")
toolbar = DebugToolbarExtension(app)
app.register_blueprint(compte)
db.init_app(app)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == "static":
        filename = values.get("filename", None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values["q"] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == "__main__":
    app.run()
