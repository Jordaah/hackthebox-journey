from functools import wraps
from flask import session, jsonify

def authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return jsonify({"error": "Go login!"}), 401
        
        return f(*args, **kwargs)
    return decorated_function