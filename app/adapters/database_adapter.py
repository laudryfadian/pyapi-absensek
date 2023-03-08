from pymongo import MongoClient

from app.config import Config


class DatabaseAdapter:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client[Config.MONGO_DBNAME]
        self.users = self.db['users']
        self.settings = self.db['settings']
        self.absent = self.db['absent']
        self.company = self.db['company']

    def get_collection(self, name):
        return self.db[name]

    def get_document_by_id(self, collection_name, document_id):
        collection = self.get_collection(collection_name)
        return collection.find_one({'_id': document_id})

    def insert_document(self, collection_name, document):
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        return result.inserted_id

    def update_document(self, collection_name, document_id, document):
        collection = self.get_collection(collection_name)
        result = collection.replace_one({'_id': document_id}, document)
        return result.modified_count > 0

    def delete_document(self, collection_name, document_id):
        collection = self.get_collection(collection_name)
        result = collection.delete_one({'_id': document_id})
        return result.deleted_count > 0