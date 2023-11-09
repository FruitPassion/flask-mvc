import os

import pymysql

# Necessaire pour la compatibilité sur Linux
pymysql.install_as_MySQLdb()


class DevConfig:
    SECRET_KEY = os.urandom(32)
    ENVIRONMENT = "development"
    FLASK_APP = "Base"
    DEBUG = True
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SECURITY_PASSWORD_SALT = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'mariadb://local_user:password@localhost:3306/db_fiches_dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
