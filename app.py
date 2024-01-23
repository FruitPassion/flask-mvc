import json
import os
import sys

from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, request, url_for, render_template
from werkzeug.exceptions import HTTPException

# Importation des controller
from controller.compte import compte
from custom_paquets.app_checker import check_config

# Importation de l'objet DB
from model.shared_model import db


# Fonction pour créer une application et la paramétrer
def create_app(config=None):
    # Vérification de la configuration demandée.
    # Si aucune configuration n'est demandée, la configuration par défaut est la configuration de développement
    check_config(config)

    # Initialisation
    app = Flask(__name__, template_folder="view")

    # Chargement de la configuration dev ou prod
    app.config.from_object(f"config.{config.capitalize()}Config")

    # Activation de la barre de debug
    # Elle permet d'afficher des informations sur les requêtes et les temps de chargement
    toolbar = DebugToolbarExtension(app)

    # Enregistrement des controller
    app.register_blueprint(compte)

    # Initialisation du schema de la base de données dans l'application
    db.init_app(app)

    # Permet de gérer les erreurs et de les afficher dans une page dédiée
    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        description = "Quelque chose s'est mal passé"
        if isinstance(e, HTTPException):
            code = e.code
            try:
                with open('static/error.json') as json_file:
                    errors = json.load(json_file)
                    description = errors[f"{code}"]["description"]
            except SystemExit as e:
                raise e
        return render_template("common/erreur.html", erreur=f"Erreur {code}",
                               description=description), code

    # Permet de forcer le rafraichissement du cache des fichiers statiques en ajoutant un timestamp à la fin de l'url
    @app.context_processor
    def override_url_for():
        return dict(url_for=dated_url_for)

    def dated_url_for(endpoint, **values):
        print(endpoint, values)
        if endpoint == "static":
            filename = values.get("filename", None)
            if filename:
                file_path = os.path.join(app.root_path, endpoint, filename)
                values["q"] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)

    return app


if __name__ == "__main__":
    # Si on lance le script directement, cela lance l'application avec la configuration par défaut
    try:
        create_app(sys.argv[1]).run()
    except IndexError:
        create_app().run()
