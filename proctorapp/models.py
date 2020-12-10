from datetime import datetime
from proctorapp import db
from sqlalchemy import Date


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sessionname = db.Column(db.DateTime, unique=True, nullable=False)
    startdate = db.Column(db.DateTime, unique=True, nullable=False)
    enddate = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"User('{self.sessionname}', '{self.startdate}', '{self.enddate}')"


class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rawData = db.Column(db.String(120), nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.sessionname}', '{self.startdate}', '{self.enddate}')"
