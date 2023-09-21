# models/venta.py
from flask_sqlalchemy import SQLAlchemy
from database import db


class Venta(db.Model):
    __tablename__ = 'venta'
    id_p = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.BigInteger, nullable=False)
    descripcion_cosas = db.Column(db.String(255), nullable=False)
    id_per = db.Column(db.Integer, db.ForeignKey('personalizacion.id_p'), nullable=False)
    id_pr = db.Column(db.Integer, db.ForeignKey('producto_almacenado.id_Pr'), nullable=False)
