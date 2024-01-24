from model.shared_model import db, SCHEMA


class ParticiperA(db.Model):
    __tablename__ = 'ParticiperA'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': SCHEMA}

    Id_Cour = db.Column(db.ForeignKey(f'{SCHEMA}.Cour.Id_Cour'), primary_key=True)
    Id_Compte = db.Column(db.ForeignKey(f'{SCHEMA}.Compte.Id_Compte'), primary_key=True)

    Compte = db.relationship('Compte', primaryjoin='ParticiperA.Id_Compte == Compte.Id_Compte', backref='participer_as')
    Cour = db.relationship('Cour', primaryjoin='ParticiperA.Id_Cour == Cour.Id_Cour', backref='participer_as')
    
    def __init__(self):
        return