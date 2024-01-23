from model.shared_model import db, Compte


def get_all_comptes():
    """
    Récupère le nom et la date de création de chaque compte

    :return: La liste des comptes
    """
    """
    A noter que on utilise pas self.nom mais Compte.nom (de meme pour date de création) pour appeler les attributs
    de la classe car il ne sont jamais initialisé dans la classe.
    """
    return Compte.query.with_entities(Compte.nom, Compte.date_creation).all()


def get_nombre_comptes():
    """
    Récupère le nombre de comptes

    :return: Le nombre de comptes
    """
    return Compte.query.count()


def get_compte_by_id(id_compte):
    """
    Récupère un compte par son id

    :param id_compte: L'id du compte
    :return: Le compte
    """
    return Compte.query.filter_by(Id_Compte=id_compte).first()
