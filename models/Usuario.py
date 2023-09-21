# models/usuario.py
from flask_sqlalchemy import SQLAlchemy
from database import db


class Usuario(db.Model):
    __tablename__ = 'usuario'  # Nombre de la tabla en la base de datos
    id_u = db.Column(db.Integer, primary_key=True)  # Define una columna de clave primaria llamada "id"
    nombre = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    tel = db.Column(db.BigInteger, nullable=False)
    n_documento = db.Column(db.BigInteger, nullable=False)
    t_Documento = db.Column(db.Enum("RC", "CC", "TI"), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    dirrecion = db.Column(db.String(255), nullable=False)  # Agregar el campo 'direccion' aquí
    rol = db.Column(db.Enum("doctor", "pac", "admin"), default="pac",nullable=True)
    contra = db.Column(db.String(255), nullable=False)
    estado_u = db.Column(db.Enum("activo", "no activo"), default="activo",nullable=True)

    def __init__(self, nombre, apellidos, edad, tel, n_documento, t_Documento, email, dirrecion,contra, rol="pac",  estado_u="activo"):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.tel = tel
        self.n_documento = n_documento
        self.t_Documento = t_Documento
        self.email = email
        self.dirrecion = dirrecion  # Agregar el campo 'direccion' aquí
        self.rol = rol
        self.contra = contra
        self.estado_u = estado_u