from flask import Blueprint, jsonify
from app.use_cases.home_use_case import HomeUseCase
from app.helpers.responses import Responses

bp = Blueprint('home_controller', __name__, url_prefix='/absent')
home_use_case = HomeUseCase()

@bp.route('/<user_id>', methods=['GET'])
def get_message_absent(user_id):
  absent = home_use_case.getMessageAbsent(user_id)
  if not absent:
    return jsonify(Responses.failedResponses(message='Gagal ambil data', code=400))
  
  return jsonify(Responses.successfullResponses(message=absent[0], data=absent[1]))