class Setting:
  def __init__(self, jamDatang=None, jamPulang=None, keterlambatan=None):
    self.jamDatang = jamDatang
    self.jamPulang = jamPulang
    self.keterlambatan = keterlambatan
    
  def to_dict(self):
    return {
      'jamDatang': self.jamDatang,
      'jamPulang': self.jamPulang,
      'keterlambatan': self.keterlambatan
    }
    
  @classmethod
  def from_dict(cls, data):
    return cls(
      jamDatang=data['jamDatang'],
      jamPulang=data['jamPulang'],
      keterlambatan=data['keterlambatan']
    )