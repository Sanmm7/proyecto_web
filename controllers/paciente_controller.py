# controllers/paciente_controller.py
from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from models import Usuario
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from database import db  # Importa la instancia de la base de datos

# Luego, en tu código, puedes acceder a la aplicación actual así:
paciente = Blueprint('paciente', __name__)


