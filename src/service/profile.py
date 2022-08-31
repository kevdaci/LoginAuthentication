from flask import jsonify, session
from database.database import User

def get_user_profile():
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        'id': user.id, 
        'email': user.email, 
        'first_name': user.first_name, 
        'last_name': user.last_name
    }), 200

