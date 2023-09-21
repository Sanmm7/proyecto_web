# models/cita.py
from flask_sqlalchemy import SQLAlchemy
from database import db


class Cita(db.Model):
    __tablename__ = 'cita'
    id_c = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    estado_c = db.Column(db.Enum('tomada', 'no tomada'), default='no tomada')
    estado_en_sistema = db.Column(db.Enum('activa', 'no activa'), default='activa')
    id_us = db.Column(db.Integer, db.ForeignKey('usuario.id_u'), nullable=False)
    id_s = db.Column(db.Integer, db.ForeignKey('sede.id_s'), nullable=False)
    id_a = db.Column(db.Integer, db.ForeignKey('agenda.id_a'), nullable=False)
    usuario = db.relationship('Usuario', backref='citas')
    sede = db.relationship("Sede", backref="citas")
    agenda = db.relationship("Agenda", backref="citas")
