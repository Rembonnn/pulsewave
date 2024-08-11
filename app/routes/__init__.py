from flask import Blueprint, jsonify
from app.controllers import user_controller

def init_routes(app):
    app.add_url_rule('/api/users', 'create_user', user_controller.create_user, methods=['POST'])
    app.add_url_rule('/api/users', 'get_users', user_controller.get_users, methods=['GET'])
    app.add_url_rule('/api/users/<int:id>', 'get_user_by_id', user_controller.get_user_by_id, methods=['GET'])
    app.add_url_rule('/api/users/<int:id>', 'update_user', user_controller.update_user, methods=['PUT'])
    app.add_url_rule('/api/users/<int:id>', 'delete_user', user_controller.delete_user, methods=['DELETE'])