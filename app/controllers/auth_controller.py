from flask import request
from app.models.user import User
from config.database import SessionLocal
from app.functions import json_web_token, response

def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return response.error(
            message="Email and password are required",
            code=400
        )

    session = SessionLocal()
    user = session.query(User).filter_by(email=email).first()

    if not user or not user.check_password(password):
        return response.error(
            message="Invalid email or password",
            code=401
        )

    token = json_web_token.create_token(user.id)
    
    return response.success(
        message="Token retrieved successfully",
        data={"token": token}
    )
