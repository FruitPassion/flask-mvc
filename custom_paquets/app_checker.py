from custom_paquets.gestion_erreurs import ConfigurationError


def check_config(config):
    """
    Vérifie la configuration demandée
    :param config: Nom de la configuration demandée
    :return: True si la configuration est valide
    """
    if config not in ["dev", "prod"]:
        raise ConfigurationError()
    return True
