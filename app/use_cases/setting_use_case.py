from app.repositories.setting_repository import SettingRepository

class settingUseCase:
  def __init__(self):
    self.settingRepository = SettingRepository()
    
  def getSetting(self):
    setting = self.settingRepository.checkSettingIsExist('63fd5b5886c9b6a1a8c67596')
    if not setting:
      return None
    
    return setting.to_dict()