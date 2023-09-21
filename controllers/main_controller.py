# controllers/main_controller.py
from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from flask_bcrypt import Bcrypt
from models import Usuario
from database import db
from flask import current_app

# Luego, en tu código, puedes acceder a la aplicación actual así:
main = Blueprint('main', __name__)
bcrypt = Bcrypt()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        edad = request.form['edad']
        tel = request.form['tel']
        n_documento = request.form['n_documento']
        t_documento = request.form['t_documento']
        email = request.form['email']
        dirrecion = request.form['dirrecion']
        contra = request.form['contra']
        hashed_password = bcrypt.generate_password_hash(contra).decode('utf-8')

        nuevo_usuario = Usuario(nombre=nombre, apellidos=apellidos, edad=edad, tel=tel, n_documento=n_documento, t_Documento=t_documento, email=email, dirrecion=dirrecion, contra=hashed_password)
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Redireccionar a la página de inicio después de registrar el usuario
        return render_template('indexalert.html')
    
    # Si la solicitud es GET, simplemente renderiza el formulario de registro
    return render_template('formregistro.html')
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        contra = request.form['password']
        user = Usuario.query.filter_by(email=email).first()
        if user:
            # Si la contraseña no está cifrada, verifica sin cifrar
         if user.contra == contra and user.email==email or (user.contra and bcrypt.check_password_hash(user.contra, contra)):
                session['user_id'] = user.id_u
                session['tipo_usuario'] = user.rol
                flash('Inicio de sesión exitoso!', 'success')
                return redirect(url_for('main.dashboard')) 
         return render_template("contramal.html")
    # If the request is GET or the login was unsuccessful, render the login page.
    return render_template("login.html")

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Has cerrado sesión exitosamente', 'info')
    return render_template('secion.html')
@main.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    tipo_usuario = session.get('tipo_usuario')
    if user_id:
        user = Usuario.query.get(user_id),Usuario.query.get(tipo_usuario)
        if tipo_usuario=='admin':
        
          return render_template('PrincipalAdmin.html', user=user)
        elif tipo_usuario=='pac':
             return render_template('PrincipalResidente.html', user=user)
        elif tipo_usuario=='doctor':
            return render_template('PrincipalVigilante.html',user=user)
    else:
     flash('Debes iniciar sesión para acceder al dashboard', 'warning')
     return render_template('index.html')