from flask import Blueprint, session
from database.database import User
from service.session import authorized
import service.profile as profile_service

profile = Blueprint("profile", __name__, url_prefix="/profile")


@profile.route('/')
@authorized
def get_user_profile():
    return profile_service.get_user_profile()

