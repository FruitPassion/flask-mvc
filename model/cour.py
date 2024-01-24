from model.shared_model import db, SCHEMA


class Cour(db.Model):
    __tablename__ = 'Cour'
    # Renseigner le bon nom de table
    __table_args__ = {'schema': SCHEMA}

    Id_Cour = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(5))
    
    def __init__(self):
        return


