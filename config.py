import os

import pymysql

# Necessaire pour la compatibilité sur Linux
pymysql.install_as_MySQLdb()


class DevConfig:
    """
    Ceci est la configuration de l'application en mode développement.
    """
    SECRET_KEY = "1234" # Utilisé pour encrypter les cookies
    ENVIRONMENT = "development" # Environnement de l'application
    FLASK_APP = "Base" # Nom de l'application
    DEBUG = True # Permet de voir les erreurs
    SESSION_PERMANENT = False # Permet de ne pas garder la session en mémoire
    SESSION_TYPE = "filesystem" # Type de session
    DEBUG_TB_INTERCEPT_REDIRECTS = False # Permet de ne pas afficher les redirections avec la barre de débogage
    DB_SCHEMA = "db_base_flask" # Nom du schéma de la base de données
    SQLALCHEMY_DATABASE_URI = f'mariadb://root:@localhost:3306/{DB_SCHEMA}' # Connexion à la base de données
    SQLALCHEMY_TRACK_MODIFICATIONS = True # Permet de suivre les modifications de la base de données avec SQLAlchemy


class ProdConfig:
    """
    Ceci est la configuration de l'application en mode production.
    """
    SECRET_KEY = os.urandom(32) # 
    ENVIRONMENT = "production"
    FLASK_APP = "Base"
    DEBUG = False
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DB_SCHEMA = "db_prod_flask"
    SQLALCHEMY_DATABASE_URI = f'mariadb://root:@localhost:3306/{DB_SCHEMA}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
