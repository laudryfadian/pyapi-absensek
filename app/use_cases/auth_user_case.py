from app.repositories.auth_repository import AuthRepository
from app.helpers.crypto import Crypto

class AuthUseCase:
  def __init__(self):
    self.repository = AuthRepository()
    
  def auth(self, email, password):
    hash = Crypto.encrypt(password)
    user = self.repository.login(email, hash)
    if not user:
      return None
    return user.to_dict()