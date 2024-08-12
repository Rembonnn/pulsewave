# app/controllers/user_controller.py
from flask import jsonify, request
from app.models.user import User
from config.database import SessionLocal
from app.functions import response

db = SessionLocal()

# Create a new user
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return response.error(message="User Not Found", code=404)

    new_user = User(name=name, email=email)
    new_user.set_password(raw_password=password)

    db.add(new_user)
    db.commit()

    return response.success(
        message="User created successfully",
        data={'name': name, 'email': email},
    )

# Get all users
def get_users():
    users = db.query(User).all()
    
    return response.success(
        message="Users retrieved successfully", 
        data=[
            {
                'id': user.id, 
                'name': user.name, 
                'email': user.email,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
            } for user in users
        ]
    )

# Get a user by ID
def get_user_by_id(id):
    user = db.query(User).filter(User.id == id).first()

    if user:
        return response.success(
            message="User retrieved successfully",
            data={'id': user.id, 'name': user.name, 'email': user.email},
        )
    
    return response.error(message="User Not Found", code=404)

# Update a user by ID
def update_user(id):
    data = request.get_json()
    user = db.query(User).filter(User.id == id).first()

    if not user:
        return response.error(message="User Not Found", code=404)
    
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)

    if 'password' in data:
        user.set_password(raw_password=data['password'])

    db.commit()

    return response.success(
        message="User updated successfully",
        data={'id': user.id, 'name': user.name, 'email': user.email},
    )

# Delete a user by ID
def delete_user(id):
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()

        return response.success(
            message="User deleted successfully",
            data={'id': user.id, 'name': user.name, 'email': user.email},
        )
    
    return response.error(message="User Not Found", code=404)
