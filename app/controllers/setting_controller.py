from flask import Blueprint, jsonify
from app.use_cases.setting_use_case import settingUseCase
from app.helpers.responses import Responses

bp = Blueprint('setting_controller', __name__, url_prefix='/settings')
setting_use_case = settingUseCase()

@bp.route('', methods=['GET'])
def get_setting():
  setting = setting_use_case.getSetting()
  if not setting:
    return jsonify(Responses.failedResponses(message='Gagal ambil setting', code=400))
  
  return jsonify(Responses.successfullResponses(message='Berhasil ambil setting', data=setting))