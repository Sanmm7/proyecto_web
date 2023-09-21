# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .Usuario import Usuario
from .Producto_almacenad import ProductoAlmacenad
from .Venta import Venta
from .Agenda import Agenda
from .Sede import Sede
from .Cita import Cita
