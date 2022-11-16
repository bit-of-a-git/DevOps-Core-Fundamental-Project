from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Will change out later
SECRET_KEY = os.urandom(32)

# Connector/Database: Will change later
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# Maybe delete this
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Will change out later
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

# figure out why this only works at the end of the file
from application import forms, models, routes