from flask import Blueprint, jsonify, request
from app.use_cases.auth_user_case import AuthUseCase
from app.helpers.responses import Responses

bp = Blueprint('auth_controller', __name__, url_prefix='/login')
auth_use_case = AuthUseCase()

@bp.route('', methods=['POST'])
def login_user():
  email = request.json['email']
  password = request.json['password']
  
  login = auth_use_case.auth(email, password)
  if not login:
    return jsonify(Responses.failedResponses('Gagal login, ulangi lagi', 400))
  
  return jsonify(Responses.successfullResponses('Berhasil login', login))