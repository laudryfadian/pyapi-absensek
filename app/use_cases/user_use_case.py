from app.entities.user_entity import User
from app.repositories.user_repository import UserRepository
from app.helpers.crypto import Crypto

class UserUseCase:
    def __init__(self):
        self.repository = UserRepository()

    def get_all_users(self):
        users = self.repository.get_all()
        return [user.to_dict() for user in users]
      
    def get_user(self, user_id):
        user = self.repository.get(user_id)
        if not user:
            return None
        return user.to_dict()

    def create_user(self, user_data):
        user = User.from_dict(user_data)
        userCheck = self.repository.checkUserIsExist(user.phone, user.email)
        if not userCheck:
            return None
        user.password = Crypto.encrypt(user.password)
        self.repository.save(user)
        return user.to_dict()

    def update_user(self, user_id, user_data):
        user_data['password'] = Crypto.encrypt(user_data['password'])
        update = self.repository.update_one(user_id, user_data)
        if not update:
            return None
        
        user = self.repository.get(user_id)
        if not user:
            return None
        
        return user.to_dict()

    def delete_user(self, user_id):
        user = self.repository.get(user_id)
        if not user:
            return None
        self.repository.delete(user)