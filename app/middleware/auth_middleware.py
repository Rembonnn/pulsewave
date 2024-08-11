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
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')

            session = SessionLocal()
            user = session.query(User).filter_by(id=user_id).first()

            if not user:
                return jsonify({'message': 'Invalid token'}), 403

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 403

        return f(*args, **kwargs)

    return decorated_function
