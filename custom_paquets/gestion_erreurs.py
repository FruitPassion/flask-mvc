class ProjectError(Exception):
    pass


class ConfigurationError(ProjectError):
    def __init__(self, message="Configuration invalide, l'argument config doit être 'dev' ou 'prod'"):
        self.message = message
        super().__init__(self.message)
