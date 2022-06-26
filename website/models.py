from flask_sqlalchemy import SQLAlchemy
from . import db

db = SQLAlchemy()

class Tokens(db.Model):
    tokenid = db.Column(db.Integer,primary_key=True)
    token = db.Column(db.String(140))
    translated = db.Column(db.String(140))
    lemmatized = db.Column(db.String(140))
    corrected = db.Column(db.String(140))
    tokenstatus = db.Column(db.String(140))
    langid = db.Column(db.String(140))
    oov = db.Column(db.String(140))
    soundex = db.Column(db.String(140))
    shortform = db.Column(db.String(140))
    namedentity = db.Column(db.String(140))