from app.adapters.database_adapter import DatabaseAdapter
from app.entities.settings_entity import Setting
from bson.objectid import ObjectId

db = DatabaseAdapter()

class SettingRepository:
  def checkSettingIsExist(self, id):
    setting = db.settings.find_one({'_id': ObjectId(id)})
    if not setting:
      return None
    
    return Setting.from_dict(setting)