# Maybe delete request if unneeded
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

# maybe delete all below if unneeded - nearly certain it's fine
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Will change out later
SECRET_KEY = os.urandom(32)

# Connector/Database: Will change later
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
# Maybe delete this
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Will change out later
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)

# figure out why this only works at the end of the file
from application import forms, models, routes
