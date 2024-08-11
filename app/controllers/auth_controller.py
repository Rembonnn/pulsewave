import os
import jwt
from datetime import datetime, timedelta
from flask import request, jsonify
from app.models.user import User
from config.database import SessionLocal

SECRET_KEY = os.getenv('SECRET_KEY')

def create_jwt_token(user_id):
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = {
        'user_id': str(user_id),
        'exp': expiration
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    session = SessionLocal()
    user = session.query(User).filter_by(email=email).first()

    if not user or user.password != password:
        return jsonify({'message': 'Invalid email or password'}), 401

    token = create_jwt_token(user.id)
    return jsonify({'token': token}), 200
