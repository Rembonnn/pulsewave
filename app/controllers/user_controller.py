# app/controllers/user_controller.py
from flask import jsonify, request
from app.models.user import User
from config.database import SessionLocal

db = SessionLocal()

def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.add(new_user)
    db.commit()
    return jsonify({'message': 'User created successfully'}), 201

def get_users():
    users = db.query(User).all()
    
    return jsonify([
        {
            'id': user.id, 
            'name': user.name, 
            'email': user.email,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
        } for user in users
    ])

def get_user_by_id(id):
    user = db.query(User).filter(User.id == id).first()
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email})
    return jsonify({'message': 'User not found'}), 404

def update_user(id):
    data = request.get_json()
    user = db.query(User).filter(User.id == id).first()
    if user:
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
        db.commit()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

def delete_user(id):
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404
