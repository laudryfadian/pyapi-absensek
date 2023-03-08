from app.repositories.auth_repository import AuthRepository
from app.helpers.crypto import Crypto

class AuthDashUseCase:
  def __init__(self):
    self.repository = AuthRepository()
    
  def authDash(self, email, password):
    hash = Crypto.encrypt(password)
    user = self.repository.login(email, hash)
    
    if not user:
      return None
    
    if user.jobType != 'admin':
      return None
    
    return user.to_dict()