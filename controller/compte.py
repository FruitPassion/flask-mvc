from flask import Blueprint, render_template, session, redirect, url_for

from custom_paquets.decorateur import login_required
from model.compte import Compte

'''
On nomme ici le controlleur comme le fichier par convention
Si on désire un autre controlleur il suffit de creer un autre fichier,
de le nommer différement (authentification.py par exemple) puis l'importer
dans app.py et de le déclarer dans les Blueprints.
'''
compte = Blueprint("compte", __name__) # On crée un controlleur que l'on nomme en général comme le fichier

'''
Possibilité d'ajouter un prefix à l'url :

compte = Blueprint("compte", __name__, url_prefix="/compte")

De cette manière toutes les urls associées a ce controller commenceront par /compte/...
'''


@compte.route("/", methods=['GET', 'POST'])
def index():
    return render_template("compte/index.html")


@compte.route("/comptes")
def comptes():
    # On récupère la liste des comptes
    tout_les_comptes = Compte.get_all_comptes()
    # On peut passer des variables à la vue
    return render_template("compte/page_comptes.html", comptes=tout_les_comptes, nb_comptes= Compte.get_nombre_comptes())


@compte.route("/connexion")
def connexion():
    session["name"] = "Utilisateur 1"
    return redirect(url_for("compte.index"))


@compte.route("/hello", methods=['GET'])
@login_required
def hello():
    return render_template("compte/hello.html")


@compte.route("/afficher/<valeur>", methods=['GET'])
def afficher(valeur):
    # On peut récupérer des paramètres dans l'url
    return valeur


@compte.route("/deconnexion")
@login_required
def deconnexion():
    session.pop("name", None)
    return redirect(url_for("compte.index"))

