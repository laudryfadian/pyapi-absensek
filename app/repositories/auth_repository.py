from app.entities.user_entity import User
from app.adapters.database_adapter import DatabaseAdapter

db = DatabaseAdapter()

class AuthRepository:
  def login(self, email, password):
    user_data = db.users.find_one({'email': email, 'password': password})
    if not user_data:
      return None
    
    company = db.company.find_one({'_id': user_data['idCompany']})
    if not company:
      return None
    
    user_data['company'] = company['name']
    
    return User.from_dict(user_data)