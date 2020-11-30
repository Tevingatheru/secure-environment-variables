import os

db_user = os.environ.get('AWS_ACCESS_KEY_ID')
db_password = os.environ.get('AWS_SECRET_ACCESS_KEY')

print(db_user)
print(db_password)
