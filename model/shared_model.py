from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Photo(db.Model):
    __tablename__ = 'Photo'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': 'db_base_flask'}

    Id_Photo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(50))
    chemin = db.Column(db.String(100), nullable=False)
    Id_Compte = db.Column(db.ForeignKey(f'db_fiches_dev.Compte.Id_Compte'), primary_key=True)

    Compte = db.relationship('Compte', primaryjoin='Photo.Id_Compte == Compte.Id_Compte', backref='photos')


class Compte(db.Model):
    __tablename__ = 'Compte'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': 'db_base_flask'}

    Id_Compte = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    date_creation = db.Column(db.DateTime, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    essaie_connexion = db.Column(db.String(50), nullable=False)
    actif = db.Column(db.Boolean, nullable=False)