from flask import Flask, Blueprint
from flask_migrate import Migrate
from controllers.main_controller import main
from controllers.admin_controller import admin
from controllers.doctor_controller import doctor
from controllers.paciente_controller import paciente
from database import db  # Importa db desde tu archivo db.py
from models import Usuario, ProductoAlmacenad,Sede,Cita,Agenda,Venta
app = Flask(__name__)
app.config['SECRET_KEY'] = '1034516961Sa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/proyectoweb'
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(main)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(doctor, url_prefix='/doctor')
app.register_blueprint(paciente, url_prefix='/paciente')

if __name__ == "__main__":
    app.run()
