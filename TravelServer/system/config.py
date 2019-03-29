
SECRET_KEY = 'dkashdlkk'
hostname = '127.0.0.1'
port = 3306
database = 'travelapp'
username = 'root'
password = '123456'

db_uri = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(username,password,hostname,port,database)

SQLALCHEMY_DATABASE_URI = db_uri

# 用来跟踪错误
SQLALCHEMY_TRACK_MODIFICATIONS = False

from datetime import timedelta
PERMANENT_SESSION_LIFETIME = timedelta(seconds=1000)