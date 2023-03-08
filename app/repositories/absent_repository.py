from app.adapters.database_adapter import DatabaseAdapter
from app.entities.absent_entity import Absent
from bson.objectid import ObjectId

db = DatabaseAdapter()

class AbsentRepository:
  def get_all(self):
    absents = db.absent.find()
    absent_list = []
    for absent in absents:
      absent_list.append(Absent(absent['_id'], absent['idUser'], absent['time'], absent['date'], absent['image'], absent['latlong'], absent['approve']))
    return absent_list
  
  def get_absent_by_iduser(self, user_id, date):
    absent_data = db.absent.find({'idUser': ObjectId(user_id), 'date': date})
    list = []
    for absent in absent_data:
      list.append(Absent(absent['_id'], absent['idUser'], absent['time'], absent['date'], absent['image'], absent['latlong'], absent['approve']))
    return list