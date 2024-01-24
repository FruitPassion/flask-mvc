<br><br>
<div align="center">
  <h1>Flask MVC</h1>
  <p>
    Documentation de développement et d'utilisation basique du framework Flask au format MVC.<br>
    <a href='https://fruitpassion.fr/' target='_blank'>Mon portfolio</a>
    <br/>
  </p>
</div>

***
<div align="center">
<img src="https://imgur.com/EPtdU76.png">
</div>

***

## Sommaire

- [Sommaire](#sommaire)
- [Architecture](#architecture)
- [Structure du projet](#structure-du-projet)
  - [Controller :](#controller-)
  - [Custom-Paquets :](#custom-paquets-)
  - [Model :](#model-)
  - [Static :](#static-)
  - [View :](#view-)
  - [app.py :](#apppy-)
  - [config.py :](#configpy-)
- [Prérequis](#prérequis)
  - [A faire : Déploiments simplifié docker pour développement](#a-faire--déploiments-simplifié-docker-pour-développement)
  - [BDD locale ](#bdd-locale-)
  - [Installation de Python 3.10 ](#installation-de-python-310-)
  - [Création de l'envrionnement virtuel ](#création-de-lenvrionnement-virtuel-)
  - [Installation des dépendances/librairies ](#installation-des-dépendanceslibrairies-)
  - [Lancement du projet](#lancement-du-projet)
- [Outils utiles](#outils-utiles)
  - [Generation des classes de la base de donnée](#generation-des-classes-de-la-base-de-donnée)

***

<div align="center">
<img src="https://imgur.com/nsEGruA.png">
</div>

***

## Architecture

Le projet suit le modèle de conception MVC. Ce concept de MVC (Model-View-Controller) dans une application web, comme
Flask, est une manière de structurer et d'organiser le code pour améliorer la clarté et la maintenabilité de
l'application. Ainsi :

- **Modèle (Model) :**
  <br>Le modèle représente les données de l'application. Il s'agit de la logique métier qui stocke, gère et manipule les
  informations. Par exemple, dans un site web de vente en ligne, le modèle pourrait gérer les produits, les utilisateurs
  et les commandes.

- **Vue (View) :**
  <br>La vue est responsable de l'interface utilisateur et de l'affichage des données aux utilisateurs. Elle s'occupe de
  la présentation des informations et de la manière dont elles sont affichées à l'écran. Dans un site web, la vue serait
  la page web que les utilisateurs voient, avec des éléments tels que les formulaires, les boutons, etc.

- **Contrôleur (Controller) :**
  <br>Le contrôleur agit comme un intermédiaire entre le modèle et la vue. Il reçoit les requêtes des utilisateurs via
  l'interface utilisateur (vue), traite ces requêtes en utilisant les données du modèle et détermine ensuite comment
  afficher les résultats à l'utilisateur. Par exemple, il gère les actions comme l'ajout d'un produit au panier dans
  un site de commerce électronique.

> [!IMPORTANT]  
> Sur le schéma, il y a la mention de routes, celles-ci sont incluses dans chaque controller en tant que méthode
> d'appel.

<br/>
<div align="center">
<img src="https://files.realpython.com/media/mvc_diagram_with_routes.e12c5b982ac8.png" alt="flask-logo" width="60%">
</div>

***

<div align="center">
<img src="https://imgur.com/SAbFj1w.png">
</div>

***

## Structure du projet

> [!NOTE]  
> Tous les dossiers contiennent le fichier .gitkeep, ce dernier permet de garder le dossier vide quand on l'envoie sur
> github. Sans cela, un dossier vide n'est pas pris en compte par le git.

Ainsi, à la racine du projet, on retrouve plusieurs fichiers et dossiers :

### Controller :

Les controller comme dit précedement, permettent à partir d'une route donnée par l'utilisateur, d'effectuer des actions
avec le model et d'afficher une vue.

Dans le fichier `/controller/compte.py` par exemple, on retrouve la route **/** dans le navigateur. Cette route est
associé  à la fonction `index()`.
On peux aussi voir que la route utilise des `methods`, ici *GET*. Si on utilise une form on pourrait utiliser `methods=['GET', 'POST']` pour indiquer que l'on souhaite traiter une form.

Ainsi quand on tape `http://localhost:5000/` dans notre navigateur, Flask effectue la fonction qui suit  nommée
`index()`.

```python
@compte.route("/", methods=['GET'])
def index():
    return render_template("/view/compte/index.html")
```

Cette fonction permet de faire un rendu du fichier `/view/compte/index.html` puis de l'envoyer à l'utilisateur. :

![return-index](https://imgur.com/828SrDv.png)

En regardant le fichier `/view/compte/index.html` dans les [View](#view) on peux voir que les trois boutons sont chacuns reliés à une route du controller `Compte`.

Il y a la route `/comptes`, la route `/afficher`, la route `/hello` et la route `/connexion`.

La route `/comptes` est tel que :

```python
@compte.route("/comptes")
def comptes():
    tout_les_comptes = Compte().get_all_comptes()
    return render_template("compte/page_comptes.html", comptes=tout_les_comptes, nb_comptes=Compte().get_nombre_comptes())
```

On à la route, la fonction associée puis on appel la fonction `get_all_comptes()` issue du [model `Compte()`](#model) et on stocke sa valeur dans la variable `tout_les_comptes`. On passe ensuite cette variable à la fonction `render_template()` à laquelle on passe aussi la fonction `get_nombre_comptes` sous le nom de nb_comptes.

> [!NOTE]  
> `render_template()` prend en arguments obligatoire le chemin d'un fichier html ainsi que le nombre d'arguments souhaités. Il est possible de passer des variables à la vue ainsi que des fonctions. Voir [View](#view).

On à ensuite la route `/afficher`. Cette route est particulière car pour fonctionner elle nécessite un paramètres dans l'URL.

```python
@compte.route("/afficher/<valeur>", methods=['GET'])
def afficher(valeur):
    return valeur
```

Ainsi, si on tape dans la barre de recherche `http://localhost:5000/afficher/test` on pourras récuperer le paramètre valeur en tant que variable et l'utiliser à notre guise (ici on l'affiche simplement).

La route `/hello` possède entre sa déclaration et sa fonction un décorateur *`@login_required`* déclaré dans le fichier `decorateurs.py` déclaré dans [custom-paquets](#custom-paquets). Ce décorateur donc est smplement une fonction appelé avant d'effectuer la fonction de la route.

```python
def decorated_function(*args, **kwargs):
    if not session.get("name"):
        return abort(403)
    return func(*args, **kwargs)
```

Ici, si on ne trouve pas la valeur `name` en session, on retourne un code 403. Les erreurs sont gérée dans le fichier [app.py](#apppy)

![403](https://imgur.com/k6dDdGd.png)

Enfin, on à la route `/connexion` qui permet d'assigner à une valeur à `name` en session.

```python
@compte.route("/connexion")
def connexion():
    session["name"] = "Utilisateur 1"
    return redirect(url_for("compte.index"))
```

On utilise la variable `session` qui est un dictionnaire et on lui assigner la valeur `"Utilisateur 1"`.
Par la suite, on rediriger l'utilisateur vers la route `/`.

> [!NOTE]  
> `url_for()` prend en argument '*`controller`*.*`fonction de route`*'. Si on voulais rediriger vers la route `/comptes`, par exemple, on aurait fait `redirect(url_for('compte.comptes'))`.
>
> Pour la route `/afficher/<parametre>`, on aurait utilisé `redirect(url_for('compte.afficher', valeur='valeur parametre'))`. Voir aussi [view](#view) ou on utilise des redirections similaires.

### Custom-Paquets :

Ce dossier contient tous les fichiers python qui ne rentre pas dans les autres dossiers.

Par exemple, `/custom_paquets/decorateur.py` contient les décorateurs qui servent de *'filtres'* aux routes, c'est à dire qui effectuent des vérifications avant d'accorder l'accès à la fonction associé à une route. Par exemple *`@login_required`* permet de vérifier si la valeur `name` est bien présente en session.


### Model :

Pour cet exemple, on utilisera cette structure de données simpliste :

![mcdi](https://imgur.com/w8vm5az.png)

Ce dossier comprend un fichier par table de la base de donnée. Ainsi on auras `compte.py`, `cour.py`, `photo.py`, etc. 

Chaque fichier comprend donc une classe au nom d'une table et contient en attributs de classe les noms de colonnes, mais précise aussi les types, les indexs, si la valeur peux être nulle, la clée primaire, etc.

Ici la table Compte dans `/model/compte.py`:

```python
class Compte(db.Model):
    __tablename__ = 'Compte'
    __table_args__ = {'schema': 'db_base_flask'}

    Id_Compte = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    date_creation = db.Column(db.DateTime, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    essaie_connexion = db.Column(db.String(50), nullable=False)
    actif = db.Column(db.Boolean, nullable=False)

    ...
```

On retrouve aussi la table photo ( `/model/photo.py`) qui possede une clée étrangère associée à la table compte.

```python
class Photo(db.Model):
    __tablename__ = 'Photo'
    __table_args__ = {'schema': 'db_base_flask'}

    Id_Photo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(50))
    chemin = db.Column(db.String(100), nullable=False)
    Id_Compte = db.Column(db.ForeignKey(f'db_base_flask.Compte.Id_Compte'), primary_key=True)

    Compte = db.relationship('Compte', primaryjoin='Photo.Id_Compte == Compte.Id_Compte', backref='photos')

    ...
```

> [!IMPORTANT]   
> La derniere ligne permet de faire la jointure interne de manière automatique si aucune autre jointure n'est précisée.


Quand on se rend sur le fichier `model/compte.py` par exemple, on peut y voir la fonction `get_all_comptes()` que
l'on a utilisé précedemment dans notre controller.

```python
def get_all_comptes(self):
    return Compte.query.with_entities(Compte.nom, Compte.date_creation).all()
```

La premiere ligne est la définition du nom de la fonction ainsi que les paramètres entre les parenthèses (il n'y en a
pas ici). La seconde ligne est la query qui pourrait se traduire comme suit en SQL:

```sql
SELECT nom, date_creation
FROM Compte;
```

On indique d'abord la classe python depuis laquelle on veut baser la selection (voir [shared-model](#shared-model)), ensuite
on appel la méthode `.query` pour dire que c'est un SELECT. Ensuite, on précise les colonnes que l'on souhaite avec
la méthode `.with_entities` (ne pas en mettre revient à faire un `SELECT *`).<br>
A la toute fin, on utilise la méthode `.all()` pour dire que l'on souhaite récupérer l'ensemble des résultats. Si on
veut le premier résultat, on aurait par exemple utilisé `.first()`, ou encore pour avoir le nombre de résultats, on
aurait  utilisé `.count()`

On retourne par la suite la query et on peux la stocker depuis l'appel tel que :

```python
comptes = Comptes().get_all_comptes()
```

La valeur retourné est ici une liste de d'objets de type `Compte`, comme on à utilisé `all()` en fin de query. Un `first()` n'aurait renvoyé qu'un seul objet de type `Compte`. 

L'accès à un attribut de la classe se fait (en reprenant la variable `compte` par exemple) comme suit :

```python
comptes = Comptes().get_all_comptes() # on récupère la liste de tout les comptes
print(comptes[0].nom) # on affiche le nom du premier compte de la liste
```


> [!NOTE]  
> Pour plus d'infos, n'hésitez à consulter
> la [documentation officielle](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/)
> ou cet article
> de [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)

### Static :

Ce dossier en contient trois autres :

- **CSS** : pour stocker tout les fichiers CSS
- **images** : pour stocker toutes les images
- **JS** : pour stocker tout les fichiers JS

On pourrait par exemple rajouter le dossier 'audio' pour stocker tous les fichiers audio.

> [!IMPORTANT]  
> Tout se qui se trouve dans le dossier static est accessible depuis le navigateur et permettras de linker vos css, js, images, etc


### View :

Situées dans le dossier `/view`, on y stoque tout les fichiers html à rendre pour l'utilisateur.

- A finir (en attendant voir les [templates](https://flask.palletsprojects.com/en/2.3.x/templating/) et [héritages de templates](https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/))

### app.py :

Fichier à exécuter pour lancer l'application. Permet d'importer les différents controller ainsi que de préciser
la configuration à utiliser.


> [!IMPORTANT]  
> Il est à noter qu'on utilise ici des "Blueprint". Ainsi quand on veux avoir un controlleur dedié à quelque chose de différent, on peux le rajouter dans le dossier controller et le réferencer dans app.py  
>
> Voir [la doc](https://flask.palletsprojects.com/en/2.2.x/blueprints/)

### config.py :

Fichier utilisé pour créer différentes paramètres différentes configurations pour l'application.
C'est notamment dans ce fichier que l'on pourras cofnigurer l'accès à la base de donnée (mariadb par défaut).

***

<div align="center">
<img src="https://imgur.com/xKbI3nf.png">
</div>

***

## Prérequis

### A faire : Déploiments simplifié docker pour développement

### BDD locale <img src="https://pic.clubic.com/v1/images/1501317/raw" height="21">

Pour faire tourner le projet, il est necessaire d'avoir une base de donnée locale. Pour cela, on utilisera MariadDB.
Vous pouvez aussi utiliser XAMPP. Vous pouvez aussi utiliser SQLite pour la portabilité. On peux paramétrer l'application dans le fichier `config.py` qui se trouve à la racine du projet.

Une fois mysql démaré, on cherchera à executer en tant que root le script `db_creation.sql` en se basant sur
[ces méthodes](https://dev.mysql.com/doc/refman/8.0/en/mysql-batch-commands.html). Ledit script permet ainsi de créer l'utilisateur nécessaire à la connexion, mais aussi de créer le
schéma de la base de donnée.

### Installation de Python 3.10 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Python_logo_01.svg/1200px-Python_logo_01.svg.png" height="20">

Le projet tournant grâce à Python, il est necessaire de l'avoir installé sur sa machine.
La verison que nous utiliserons ici est la 3.10, elle est installable via
[ce lien](https://www.python.org/downloads/release/python-31011/)

Pour connaitre la version que l'on possède du langage, il suffit de taper `python --version` dans son terminal.
Si jamais vous posseder plusieurs versions, il suffit de tapper la version désirée pour la lancer.
Ainsi, si par exemple, je possède python 3.8 et 3.10, et que je veux lancer la 3.10 je taperai simplement `python3.10`
dans le terminal pour lancer un programme `.py` avec cette version.

Sinon, si on ne possède qu'une seule version, on peut
juste utiliser `python` ou `python3`.

### Création de l'envrionnement virtuel <img src="https://imgur.com/xBG59oA.png" height="20">

Un environnement virtuel en Python est comme une boîte de rangement virtuelle qui isole et organise les bibliothèques et
les dépendances spécifiques à un projet Python. Cela permet de travailler sur différents projets sans qu'ils
interfèrent les uns avec les autres, garantissant ainsi un développement propre et sans conflits. Chaque boîte de
rangement virtuelle contient les ressources nécessaires à un projet, assurant une gestion facile et une portabilité
pour collaborer avec d'autres développeurs.

Pour le projet, on créera un environnement virtuel en se plaçant dans le projet git.
Depuis ce projet, on ouvre le terminal et on tape :
`python -m venv .env`. Au bout de quelques secondes un dossier nommé `.env` est créé à la racine du projet.
C'est le dossier de notre environnement virtuel.

Maintenant, pour activer cet environnement, il suffit de taper la commande (voir [pour chaque OS](https://docs.python.org/3/library/venv.html)):

```shell
$ .env\Scripts\activate
``` 

Dans le terminal, devrait alors apparaitre `(.env)` au début de la ligne.

![img.png](https://imgur.com/he2zP1V.png)

Cela, signifie que l'envrionnement est maintenant activé et que toutes les installations que vous ferez seront stocké
dans l'envrionnement et pas directement sur votre machine.

> [!NOTE]  
> Quand vous lancerez de nouveau votre terminal, selon votre IDE, l'envrionnement s'activera automatiquement. Pensez à
> toujours vérifier

### Installation des dépendances/librairies <img src="https://seeklogo.com/images/P/python-package-index-logo-F2EC9F1F8C-seeklogo.com.png" height="20">

Maintenant que notre environnement virtuel est pret, il suffit de lui installer les dépendances et librairies.
Celles-ci sont stockées à la racine du projet dans le fichier `requirements.txt`, ainsi quand vous ajouterez une
librairie au projet, vous devrez aussi l'ajouter dans le `requirements.txt`.

L'installation des librairires se fait avec la commande pip en se placant à la racine du projet et avec l'envrionnement
virtuel activé.

```shell
(.env) $ pip install -r requirements.txt
``` 

Si tout se passe bien, à la fin de l'execution de la commande, le projet sera enfin prêt à être lancé.

### Lancement du projet

Le lancement s'effectue grâce au fichier `app.py` que l'on lance à la racine du projet avec l'environnement virtuel
activé.

```shell
(.env) $ python app.py
``` 

On peut ensuite se rendre sur son navigateur web et acceder à l'index via `http://localhost:5000/`
ou `http://127.0.0.1:5000/`


***

<div align="center">
<img src="https://imgur.com/0wG0ZGL.png">
</div>

***

## Outils utiles

### Generation des classes de la base de donnée

La librairie [flask-sqlacodegen](https://pypi.org/project/flask-sqlacodegen/) permet à partir d'une connexion à une base de donnée de générer les tables au format de classe pour SQLAlchemy





