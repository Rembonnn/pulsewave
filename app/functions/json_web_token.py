import os
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = os.getenv('SECRET_KEY')

def create_token(user_id):
    expiration = datetime.now(timezone.utc) + timedelta(minutes=15)

    payload = {
        'user_id': str(user_id),
        'exp': expiration
    }

    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')