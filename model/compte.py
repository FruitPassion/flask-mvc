from custom_paquets.converter import convertToDict
from model_db.shared_model import db
from model_db.compte import Compte

def getAllPersonnel():
    """
    Récupère l'id, nom, prenom et role de chaque membre du personnel

    :return: La liste des membres du personnel
    """
    compte = Compte.query.with_entities(Compte.Id_Compte, Compte.nom, Compte.date_creation, Compte.actif).all()
    return convertToDict(compte)
