from models.user import User
from models.leave import Leave
from datetime import date
from mongoengine.errors import NotUniqueError
from models import storage
import bcrypt

password = '5555555555'

h_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

objects1 = {
        'staff_number': 'NCT8649',
        'first_name': 'Samuel',
        'last_name': 'Affum',
        'email': 'sam@mail.com',
        'password': h_pwd,
        'date_of_birth': date(2020, 8, 25).isoformat(),
        'phone': '0215122652',
        'SSNIT': 'HFT554555',
        'NID': '5565236524',
        'employment_date': date(2020, 8, 25).isoformat(),
        'gender': 'Male',
        'department': 'IT',
        'position': 'Software engineer',
        'Superuser': True
        }

objects2 = {
        'staff_number': 'NCT2111',
        'first_name': 'Roy',
        'last_name': 'Efe',
        'email': 'rose@mail.com',
        'password': h_pwd,
        'date_of_birth': date(2020, 8, 25).isoformat(),
        'phone': '08077763334',
        'SSNIT': 'HFT56324',
        'NID': '5565632656',
        'employment_date': date(2020, 8, 25).isoformat(),
        'gender': 'Female',
        'department': 'Project',
        'position': 'PMO',
        'Superuser': False
        }

objects3 = {
        'staff_number': 'NCT5311',
        'first_name': 'mary',
        'last_name': 'Ebe',
        'email': 'roz@gmail.com',
        'password': h_pwd,
        'date_of_birth': date(2020, 8, 25).isoformat(),
        'phone': '08077763334',
        'SSNIT': 'HFT729324',
        'NID': '5565632656',
        'employment_date': date(2020, 8, 25).isoformat(),
        'gender': 'Female',
        'department': 'Project',
        'position': 'PMO',
        }

storage.connect()

user = User(**objects1)
user2 = User(**objects2)
user3 = User(**objects3)
try:
    id1 = storage.save(user)
    id2 = storage.save(user2)
    id3 = storage.save(user3)
    print(id1, id2, id3)
except Exception as e:
	print(e)
