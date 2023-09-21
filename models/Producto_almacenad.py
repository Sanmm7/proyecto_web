# models/producto_almacenado.py
from flask_sqlalchemy import SQLAlchemy
from database import db


class ProductoAlmacenad(db.Model):
    __tablename__ = 'producto_almacenad'
    id_Pr = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)
    lente = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False, default=1)

    def actualizar(self, nuevos_valores):
        for campo, valor in nuevos_valores.items():
            setattr(self, campo, valor)
