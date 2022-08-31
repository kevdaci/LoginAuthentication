from flask import session
from constants.login_messages import IN_SESSION, USER_UNAUTHORIZED

def authorized(func):
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            return USER_UNAUTHORIZED, 403
        else:
            return func(*args, **kwargs)
    wrapper.__name__  = func.__name__
    return wrapper

def in_session(func):
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return IN_SESSION, 409
        else:
            return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
        