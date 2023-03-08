from flask import Blueprint, jsonify, request
from app.use_cases.user_use_case import UserUseCase
from app.helpers.responses import Responses

bp = Blueprint('user_controller', __name__, url_prefix='/users')
user_use_case = UserUseCase()

@bp.route('', methods=['GET'])
def get_all_users():
    users = user_use_case.get_all_users()
    return jsonify(Responses.successfullResponses(message='Berhasil menampilkan users', data=users))

@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_use_case.get_user(user_id)
    
    if not user:
        return jsonify(Responses.failedResponses(message='User tidak ada', code=400))
    
    return jsonify(Responses.successfullResponses(message='Berhasil menampilkan user', data=user))

@bp.route('', methods=['POST'])
def create_user():
    user_data = request.json
    user = user_use_case.create_user(user_data)
    
    if not user:
        return jsonify(Responses.failedResponses(message='User sudah ada', code=400))
    
    res = {
        'email': user.get('email')
    }
    
    return jsonify(Responses.successfullResponses(message='Berhasil membuat user', data=res))
  
@bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    user = user_use_case.update_user(user_id, user_data)
    if not user:
        return jsonify(Responses.failedResponses(message='Update gagal', code=400))
    return jsonify(Responses.successfullResponses(message='Berhasil update user', data=user))

@bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = user_use_case.get_user(user_id)
    if not user:
        return jsonify(Responses.failedResponses(message='User tidak ada', code=400))
    
    user_use_case.delete_user(user_id)
    if not user_use_case:
        return jsonify(Responses.failedResponses(message='Gagal menghapus', code=400))
    
    return jsonify(Responses.successfullResponses(message='Berhasil menghapus user', data=None))