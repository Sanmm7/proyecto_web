# models/agenda.py
from flask_sqlalchemy import SQLAlchemy
from database import db


class Agenda(db.Model):
    __tablename__ = 'agenda'
    id_a = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fecha_hora_inicial = db.Column(db.DateTime, nullable=False)
    fecha_hora_final = db.Column(db.DateTime, nullable=False)
    id_doctor = db.Column(db.Integer, db.ForeignKey('usuario.id_u'), nullable=False)
    doctor = db.relationship('Usuario', backref=db.backref('agendas', lazy=True))

    def __init__(self, fecha_hora_inicial, fecha_hora_final, id_doctor):
        self.fecha_hora_inicial = fecha_hora_inicial
        self.fecha_hora_final = fecha_hora_final
        self.id_doctor = id_doctor
