from app.entities.settings_entity import Setting
from app.repositories.setting_repository import SettingRepository
from app.repositories.user_repository import UserRepository
from app.repositories.absent_repository import AbsentRepository
from app.helpers.crypto import Crypto
import datetime
import pytz
import locale

# Set the locale to Indonesian
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

class HomeUseCase:
  def __init__(self):
    self.settingRepository = SettingRepository()
    self.userRepository = UserRepository()
    self.absentRepository = AbsentRepository()
    
  def getMessageAbsent(self, user_id):
    timezone = pytz.timezone("Asia/Jakarta")
    date_now = datetime.datetime.now(timezone).strftime("%A, %d %B %Y")
    time_now = datetime.datetime.now(timezone).strftime("%H%M")
    time_now = int(time_now)
    
    settingCheck = self.settingRepository.checkSettingIsExist('63fd5b5886c9b6a1a8c67596')
    if not settingCheck:
      return None
    
    user = self.userRepository.get(user_id)
    if not user:
      return None
    
    absen = {
      'masuk': False,
      'pulang': False
    }
    
    result = []
    
    check = self.absentRepository.get_absent_by_iduser(user_id, date_now)
    
    if not user.isAbsen:
      if time_now <= int(settingCheck.jamDatang):
        return 'Belum saatnya absen yaa', absen
      
      elif time_now <= int(settingCheck.jamDatang) + int(settingCheck.keterlambatan):
        absen['masuk'] = True
        return 'Sudah saatnya absen', absen
      
      elif len(check) == 2:
        return 'Selamat beristirahat', absen
      
      absen['masuk'] = True
      return 'Kamu telat !!!', absen
    else:
      print("true ini")
    # if not user.isAbsen:
    #   if time_now <= int(settingCheck.jamDatang):
    #     print(1)
    #     return 'Belum saatnya absen yaa', absen
      
    #   elif time_now -1 <= int(settingCheck.jamDatang) + int(settingCheck.keterlambatan) - 1:
    #     absen.masuk = True
    #     print(2)
    #     return 'Sudah saatnya absen', absen
      
    #   elif time_now >= int(settingCheck.jamDatang) + int(settingCheck.jamPulang):
    #     absen.masuk = True
        
    #     if len(check) == 2:
    #       print(3)
    #       return 'Selamat beristirahat', absen
        
    #     print(4)
    #     return 'Kamu telat !!!', absen
    # if user.isAbsen:
    #   if time_now >= int(settingCheck.jamPulang):
    #     absen.pulang = True 
    #     print(5)
    #     return 'Saatnya absen pulang', absen  
    #   print(6)
    #   return 'Semangat kerjanya !!', absen
    # print("hehe")
    
      
      