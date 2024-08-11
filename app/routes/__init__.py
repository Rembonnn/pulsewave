from flask import Blueprint, jsonify
from app.controllers import user_controller, auth_controller
from app.middleware.auth_middleware import token_required

def init_routes(app):
    # Routes tanpa otentikasi JWT
    app.add_url_rule('/api/login', 'login', auth_controller.login_user, methods=['POST'])
    
    # Routes yang dilindungi dengan otentikasi JWT
    app.add_url_rule('/api/users', 'create_user', token_required(user_controller.create_user), methods=['POST'])
    app.add_url_rule('/api/users', 'get_users', token_required(user_controller.get_users), methods=['GET'])
    app.add_url_rule('/api/users/<int:id>', 'get_user_by_id', token_required(user_controller.get_user_by_id), methods=['GET'])
    app.add_url_rule('/api/users/<int:id>', 'update_user', token_required(user_controller.update_user), methods=['PUT'])
    app.add_url_rule('/api/users/<int:id>', 'delete_user', token_required(user_controller.delete_user), methods=['DELETE'])