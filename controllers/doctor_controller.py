# controllers/doctor_controller.py
from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from models import Usuario
from database import db  # Importa la instancia de la base de datos

# Luego, en tu código, puedes acceder a la aplicación actual así:
doctor = Blueprint('doctor', __name__)

