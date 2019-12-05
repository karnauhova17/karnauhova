from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "fio": self.fio}


class Mentor(db.Model):
    __tablename__ = 'mentor'
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "fio": self.fio}


class TrainingType(db.Model):
    __tablename__ = 'trainingtype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}


class Visit(db.Model):
    __tablename__ = 'visit'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, ForeignKey('client.id'))
    mentor_id = db.Column(db.Integer, ForeignKey('mentor.id'))
    trainingtype_id = db.Column(db.Integer, ForeignKey('trainingtype.id'))
    visit_date = db.Column(db.DateTime)
    client = relationship('Client')

    def json(self):
        return {"id": self.id, "client_id": self.client_id, "mentor_id": self.mentor_id, "trainingtype_id": self.trainingtype_id, "client": self.client.json()}
