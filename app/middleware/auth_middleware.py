import os
import jwt
from flask import request, jsonify
from functools import wraps
from config.database import SessionLocal
from app.models.user import User

SECRET_KEY = os.getenv('SECRET_KEY')

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)

        if auth_header:
            try:
                token_type, token = auth_header.split()
                if token_type != 'Bearer':
                    return jsonify({'message': 'Invalid token type'}), 403
            except ValueError:
                return jsonify({'message': 'Invalid Authorization header format'}), 403

            try:
                decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                request.user = decoded_token
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 403
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 403
        else:
            return jsonify({'message': 'Token is missing'}), 403

        return f(*args, **kwargs)

    return decorated_function
