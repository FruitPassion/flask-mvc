from model.shared_model import db, SCHEMA


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
    
    @staticmethod
    def get_all_comptes():
        """
        Récupère le nom et la date de création de chaque compte

        :return: La liste des comptes
        """
        return Compte.query.with_entities(Compte.nom, Compte.date_creation).all()

    @staticmethod
    def get_nombre_comptes():
        """
        Récupère le nombre de comptes

        :return: Le nombre de comptes
        """
        return Compte.query.count()

    @staticmethod
    def get_compte_by_id(id_compte):
        """
        Récupère un compte par son id

        :param id_compte: L'id du compte
        :return: Le compte
        """
        return Compte.query.filter_by(Id_Compte=id_compte).first()
