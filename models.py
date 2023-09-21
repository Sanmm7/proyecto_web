from flask_sqlalchemy import SQLAlchemy
# Otros modelos de datos (Sede, Agenda, Cita, etc.) deben definirse de manera similar
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

    def __init__(self, nombre, apellidos, edad, tel, n_documento, t_Documento, email, dirrecion,contra, rol="paciente",  estado_u="activo"):
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
class ProductoAlmacenado(db.Model):
    __tablename__ = 'producto_almacenad'
    id_Pr = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)
    lente = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False, default=1)
    
    def actualizar(self, nuevos_valores):
        # Actualizar los campos del objeto con los nuevos valores
        for campo, valor in nuevos_valores.items():
            setattr(self, campo, valor)
class Venta(db.Model):
    __tablename__ = 'venta'

    id_p = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.BigInteger, nullable=False)
    descripcion_cosas = db.Column(db.String(255), nullable=False)
    id_per = db.Column(db.Integer, db.ForeignKey('personalizacion.id_p'), nullable=False)
    id_pr = db.Column(db.Integer, db.ForeignKey('producto_almacenado.id_Pr'), nullable=False)    