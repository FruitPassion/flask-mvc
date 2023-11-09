from model_db.shared_model import db


class Photo(db.Model):
    __tablename__ = 'Photo'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': 'db_base_flask'}

    Id_Photo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(50))
    chemin = db.Column(db.String(100), nullable=False)
    Id_Compte = db.Column(db.ForeignKey(f'db_fiches_dev.Compte.Id_Compte'), primary_key=True)

    Compte = db.relationship('Compte', primaryjoin='Photo.Id_Compte == Compte.Id_Compte', backref='photos')

