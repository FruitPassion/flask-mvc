from functools import wraps

from flask import session, abort, url_for, redirect

# Decorateur pour les pages qui necessitent une connexion
# Se place au dessus de la fonction et en dessous de la route sous le format:  @login_required
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get("name"):
            return abort(403)
        return func(*args, **kwargs)
    return decorated_function

