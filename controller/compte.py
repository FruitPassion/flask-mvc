from flask import Blueprint, render_template

compte = Blueprint("compte", __name__)
'''
Possibilité d'ajouter un prefix à l'url :

compte = Blueprint("compte", __name__, url_prefix="/compte")

De cette manière toutes les urls associées a ce controller commenceront par /compte/...
'''


@compte.route("/", method=['GET', 'POST'])
def index():
    return render_template("compte/index.html")


@compte.route("/hello")
def index():
    return "Hello"
