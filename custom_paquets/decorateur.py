from functools import wraps

from flask import session, abort


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get("name"):
            abort(403)
        return func(*args, **kwargs)

