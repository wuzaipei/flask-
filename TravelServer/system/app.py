from flask import Flask,render_template,redirect
app = Flask(__name__,static_folder='../static',static_url_path='/static',template_folder='../templates')
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app.config.from_object('system.config')

db = SQLAlchemy(app)

from system.Routes import *

@app.route('/')
def shouye():
    return 'Hello World!'
