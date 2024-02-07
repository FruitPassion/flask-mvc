from model.shared_model import db, SCHEMA


class Photo(db.Model):
    __tablename__ = 'Photo'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': SCHEMA}
    
    Id_Photo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(50))
    chemin = db.Column(db.String(100), nullable=False)
    Id_Compte = db.Column(db.ForeignKey(f'{SCHEMA}.Compte.Id_Compte'), primary_key=True)

    Compte = db.relationship('Compte', primaryjoin='Photo.Id_Compte == Compte.Id_Compte', backref='photos')
    
