from app.adapters.database_adapter import DatabaseAdapter
from app.entities.user_entity import User
from bson.objectid import ObjectId

db = DatabaseAdapter()

class UserRepository:
    def get(self, user_id):
        user_data = db.users.find_one({'_id': ObjectId(user_id)})
        if not user_data:
            return None
        return User.from_dict(user_data)
    
    def checkUserIsExist(self, phone, email):
        phoneNumber = db.users.find_one({'phone': phone})
        if phoneNumber:
            return False
        
        addressEmail = db.users.find_one({'email': email})
        if addressEmail:
            return False
        
        return True
    
    def get_all(self):
        users = db.users.find()
        user_list = []
        for user in users:
            company = db.company.find_one(user['idCompany'])
            user_list.append(User(user['_id'], user['name'], user['email'], user['password'], user['phone'], user['job'], user['superUser'], user['salary'], user['isAbsen'], user['jobType'], company['name']))
        return user_list

    def save(self, user):
        user_data = user.to_dict()
        del user_data['id']
        result = db.users.insert_one(user_data)
        user.id = result.inserted_id
        
    def update_one(self, user_id, updated_user_data):
        updated_user = {"$set": updated_user_data}
        result = db.users.update_one({"_id": ObjectId(user_id)}, updated_user)
        if not result:
            return None 

        return result

    def delete(self, user):
        oke = db.users.delete_one({'_id': ObjectId(user.id)})
        print(oke)