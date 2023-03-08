import hmac 
import hashlib
from app.config import Config

class Crypto:
  def encrypt(text):
    h = hmac.new(Config.KEY, text.encode('utf-8'), hashlib.sha256).hexdigest()
    
    return h