from flask import Blueprint, render_template

compte = Blueprint("compte", __name__)
'''
Possibilité d'ajouter un prefix à l'url :

compte = Blueprint("compte", __name__, url_prefix="/compte")

De cette manière toutes les urls associées a ce controller commenceront par /compte/...
'''


@compte.route("/", methods=['GET', 'POST'])
def index():
  prenoms = ["michel", "benoit", "andre"]
  return render_template("compte/index.html", prenoms=prenoms)


@compte.route("/hello")
def hello():
    return "Hello"
