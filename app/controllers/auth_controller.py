from flask import request, jsonify
from app.models.user import User
from config.database import SessionLocal
from app.functions import json_web_token

def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    session = SessionLocal()
    user = session.query(User).filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid email or password'}), 401

    token = json_web_token.create_token(user.id)
    
    return jsonify({'token': token}), 200
