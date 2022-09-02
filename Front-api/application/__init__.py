from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)

MYSQL_ROOT_PASSWORD = "Root"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{getenv('root')}@mysql:3306/eventsdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes