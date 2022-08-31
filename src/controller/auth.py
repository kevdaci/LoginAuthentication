from flask import Blueprint, request
from service.session import authorized, in_session
import service.auth as auth_service

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.post('/register')
def register():
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    return auth_service.register(email, password, first_name, last_name)

@auth.post('/login')
@in_session
def login():
    email = request.json['email']
    password = request.json['password']
    return auth_service.login(email, password)

@auth.post('/logout')
@authorized
def logout():
    return auth_service.logout()

    






