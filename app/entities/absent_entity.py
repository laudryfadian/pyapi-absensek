class Absent:
  def __init__(self, id=None, idUser=None, info=None, time=None, date=None, image=None, latlong=None, approve=None):
    self.id = id
    self.idUser = idUser
    self.time = time
    self.date = date
    self.image = image
    self.latlong = latlong
    self.approve = approve
    
  def to_dict(self):
    return {
      'id': str(self.id),
      'idUser': self.idUser,
      'time': self.time,
      'date': self.date,
      'image': self.image,
      'latlong': self.latlong,
      'approve': self.approve
    }
    
  @classmethod
  def from_dict(cls, data):
    return cls(
      id=data.get('_id'),
      idUser=data['idUser'],
      time=data['time'],
      date=data['date'],
      image=data['image'],
      latlong=data['latlong'],
      approve=data['approve']
    )
    