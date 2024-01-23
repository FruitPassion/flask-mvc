from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

SCHEMA = 'db_base_flask'


class ParticiperA(db.Model):
    __tablename__ = 'ParticiperA'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': SCHEMA}

    Id_Cour = db.Column(db.ForeignKey(f'{SCHEMA}.Cour.Id_Cour'), primary_key=True)
    Id_Compte = db.Column(db.ForeignKey(f'{SCHEMA}.Compte.Id_Compte'), primary_key=True)

    Compte = db.relationship('Compte', primaryjoin='ParticiperA.Id_Compte == Compte.Id_Compte', backref='participer_as')
    Cour = db.relationship('Cour', primaryjoin='ParticiperA.Id_Cour == Cour.Id_Cour', backref='participer_as')


class Compte(db.Model):
    __tablename__ = 'Compte'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': SCHEMA}

    Id_Compte = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    date_creation = db.Column(db.DateTime, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    essaie_connexion = db.Column(db.String(50), nullable=False)
    actif = db.Column(db.Boolean, nullable=False)


class Photo(db.Model):
    __tablename__ = 'Photo'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': SCHEMA}

    Id_Photo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(50))
    chemin = db.Column(db.String(100), nullable=False)
    Id_Compte = db.Column(db.ForeignKey(f'{SCHEMA}.Compte.Id_Compte'), primary_key=True)

    Compte = db.relationship('Compte', primaryjoin='Photo.Id_Compte == Compte.Id_Compte', backref='photos')


class Cour(db.Model):
    __tablename__ = 'Cour'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': SCHEMA}

    Id_Cour = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(5))