from functools import wraps
from flask import request, jsonify

# https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#custom-request-headers
def csrf_protection(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        csrf_header = request.headers.get("X-SPACE-NO-CSRF")
        if csrf_header != "1":
            return jsonify({"error": "Invalid csrf token!"}), 403
        
        return f(*args, **kwargs)
    return decorated_function