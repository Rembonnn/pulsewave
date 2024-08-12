from flask import jsonify

def success(message="Success", data=None, code=200):
    return jsonify({
        'ok': True,
        'code': code,
        'message': message,
        'data': data,
    }), code

def error(message="Error", data=None, code=500):
    return jsonify({
        'ok': False,
        'code': code,
        'message': message,
        'data': data,
    }), code