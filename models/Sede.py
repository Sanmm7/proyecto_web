# models/sede.py
from flask_sqlalchemy import SQLAlchemy
from database import db


class Sede(db.Model):
    __tablename__ = 'sede'
    id_s = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    n_trabajadores = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.BigInteger, nullable=False)
