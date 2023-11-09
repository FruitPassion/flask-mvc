from model_db.shared_model import db


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

