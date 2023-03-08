from flask import Blueprint, jsonify, request
from app.use_cases.auth_dash_use_case import AuthDashUseCase
from app.helpers.responses import Responses

bp = Blueprint('auth_dash_controller', __name__, url_prefix='/dash/login')
auth_use_case = AuthDashUseCase()

@bp.route('', methods=['POST'])
def login_user():
  email = request.json['email']
  password = request.json['password']
  
  login = auth_use_case.authDash(email, password)
  if not login:
    return jsonify(Responses.failedResponses('Gagal login, ulangi lagi', 400))
  
  return jsonify(Responses.successfullResponses('Berhasil login', login))