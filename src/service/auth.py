from flask import jsonify, session
from constants.login_messages import USER_AUTHENTICATED, USER_LOGGED_OUT, USER_UNAUTHENTICATED
from database.database import db
from database.database import User
from werkzeug.security import check_password_hash, generate_password_hash
import constants.account_requirements as ACCOUNT_REQUIREMENTS
import validators


def register(email, password, first_name, last_name):
    error_response = check_credentials(email, password)
    response = None
    if error_response is not None:
        response = error_response
    else:
        hashed_password = generate_password_hash(password)
        user = User(email=email, password=hashed_password, first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()
        response = jsonify({ 
            'message': 'User registered',
            'user': {
                'email': user.email 
            }
        }), 201
    return response

def login(email, password):
    user = User.query.filter_by(email=email).first()
    response = None
    if user is None:
        response = USER_UNAUTHENTICATED, 401
    else:
        if(check_password_hash(user.password, password)):
            session['user_id'] = user.id
            response = USER_AUTHENTICATED, 200
        else: 
            response = USER_UNAUTHENTICATED, 401
    return response

def logout():
    session.pop('user_id', default=None)
    return USER_LOGGED_OUT, 200

def check_credentials(email, password):
    error_response = None
    if not validators.email(email):
        error_response = ACCOUNT_REQUIREMENTS.INVALID_EMAIL_ERROR, 400
    if User.query.filter_by(email=email).first() is not None:
        error_response = ACCOUNT_REQUIREMENTS.EMAIL_EXIST_ERROR, 409
    if len(password) < ACCOUNT_REQUIREMENTS.PASSWORD_LENGTH:
        error_response = ACCOUNT_REQUIREMENTS.PASSWORD_LENGTH_ERROR, 400
    if ' ' in password:
        error_response = ACCOUNT_REQUIREMENTS.PASSWORD_SPACE_ERROR, 400
    return error_response