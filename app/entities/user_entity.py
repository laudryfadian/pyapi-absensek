from datetime import datetime

class User:
    def __init__(self, id=None, name=None, email=None, password=None, phone=None, job=None, superUser=None, salary=None, isAbsen=None, jobType=None, company=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.job = job
        self.superUser = superUser
        self.salary = salary
        self.isAbsen = isAbsen
        self.jobType = jobType
        self.company = company
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'job': self.job,
            'superUser': self.superUser,
            'salary': self.salary,
            'isAbsen': self.isAbsen,
            'jobType': self.jobType,
            'company': self.company,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('_id'),
            name=data['name'],
            email=data['email'],
            password=data['password'],
            phone=data['phone'],
            job=data['job'],
            superUser=data['superUser'],
            salary=data['salary'],
            isAbsen=data['isAbsen'],
            jobType=data['jobType'],
            company=data['company'],
            created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
            updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        )

    # def update_from_dict(cls, data):
    #     # if 'name' in data:
    #     #     cls.name = data['name']
    #     # if 'email' in data:
    #     #     cls.email = data['email']
    #     # cls.updated_at = datetime.utcnow()
        
    #     return cls(
    #         name=data['name'] if 'name' in data else '',
    #         email=data['email'] if 'email' in data else '',
    #         updated_at=datetime.utcnow()
    #     )