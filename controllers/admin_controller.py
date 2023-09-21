# controllers/admin_controller.py
from flask import Blueprint, jsonify, render_template, request, redirect, session, flash, url_for
from models import Usuario, ProductoAlmacenad, Agenda
from database import db
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import current_app

# Luego, en tu código, puedes acceder a la aplicación actual así:
admin = Blueprint('admin', __name__)
bcrypt = Bcrypt()

##############
@admin.route('/inventario')
def inventario():
    user_id = session.get('user_id')
    tipo_usuario = session.get('tipo_usuario')

    if user_id and tipo_usuario=="admin":
      productos = ProductoAlmacenad.query.all()
      return render_template('inventario.html', productos=productos)
    else:
          flash('Debes iniciar sesión para acceder al dashboard', 'warning')
          return render_template('index.html')
#metodo consultas
@admin.route('/optometras')
def optometras():
    user_id = session.get('user_id')
    tipo_usuario = session.get('tipo_usuario')
    if user_id and tipo_usuario=="admin":
      usuarios = Usuario.query.filter(Usuario.rol.in_(["doctor", "admin"]), Usuario.estado_u == "activo").all()
      return render_template('optometras.html', optometras=usuarios)
    else:
         flash('Debes iniciar sesión para acceder al dashboard', 'warning')
         return render_template('index.html')
######
@admin.route('/registro_doctor', methods=['GET', 'POST'])
def registro_doctor():
    if request.method == 'POST':
        # Verifica si el usuario actual es un administrador
        if session.get('tipo_usuario') == 'admin':
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
          rol = request.form['rol']  # Obtiene el valor del campo de selección de rol


            # Hash de la contraseña
          hashed_password = bcrypt.generate_password_hash(contra).decode('utf-8')

          nuevo_usuario = Usuario(
            nombre=nombre,
            apellidos=apellidos,
            edad=edad,
            tel=tel,
            n_documento=n_documento,
            t_Documento=t_documento,
            email=email,
            dirrecion=dirrecion,
            contra=hashed_password,
            rol=rol  # Asigna el rol según el valor del campo de selección
         )

          db.session.add(nuevo_usuario)
          db.session.commit()

            # Redireccionar a la página de inicio después de registrar el doctor
          return render_template('dashadminaler.html')
        else:
            flash('No tienes permisos para registrar doctores, ni administradores', 'danger')
            return redirect(url_for('index.html'))

    # Si la solicitud es GET, simplemente renderiza el formulario de registro
    return render_template('formregistro_doctor.html')
@admin.route('/editar_doctor/<int:id>', methods=['GET', 'POST'])
def editar_doctor(id):
    # Verifica si el usuario actual es un administrador
    if session.get('tipo_usuario') != 'admin':
        flash('No tienes permisos para editar doctores', 'danger')
        return redirect(url_for('/'))

    # Busca el doctor en la base de datos por su ID
    doctor = Usuario.query.get(id)

    if request.method == 'POST':
        # Obtiene los datos del formulario de edición
        doctor.nombre = request.form['nombre']
        doctor.apellidos = request.form['apellidos']
        doctor.edad = request.form['edad']
        doctor.tel = request.form['tel']
        doctor.n_documento = request.form['n_documento']
        doctor.t_Documento = request.form['t_documento']
        doctor.email = request.form['email']
        doctor.dirrecion = request.form['dirrecion']
        doctor.rol = request.form['rol']
        # Guarda los cambios en la base de datos
        db.session.commit()

        flash('Los cambios se guardaron correctamente', 'success')
        return render_template('dashadminaler.html')

    # Renderiza el formulario de edición con los datos del doctor
    return render_template('editar_doctor.html', doctor=doctor)
@admin.route('/eliminar_doctor/<int:id>', methods=['POST'])
def eliminar_doctor(id):
    # Verifica si el usuario actual es un administrador
    if session.get('tipo_usuario') != 'admin':
        flash('No tienes permisos para eliminar doctores', 'danger')
        return redirect(url_for('main./'))

    # Busca el doctor en la base de datos por su ID
    doctor = Usuario.query.get(id)

    if doctor:
        # Cambia el estado del doctor a "desactivado"
        doctor.estado_u = 'no activo'
        db.session.commit()
        flash('El doctor ha sido desactivado correctamente', 'success')
        return render_template('desacti.html')
    else:
        flash('Doctor no encontrado', 'danger')

    return redirect(url_for('admin.optometras'))
@admin.route('/pacientes')
def pacientes():
    user_id = session.get('user_id')
    tipo_usuario = session.get('tipo_usuario')
    if user_id and tipo_usuario=="admin":
      usuarios = Usuario.query.filter_by(rol="pac").all()

      return render_template('pacientes.html', optometras=usuarios)
    else:
         flash('Debes iniciar sesión para acceder al dashboard', 'warning')
         return render_template('index.html')
@admin.route('/agendas')
def agendas():
    user_id = session.get('user_id')
    tipo_usuario = session.get('tipo_usuario')
     
    if user_id and tipo_usuario == "admin":
        # Realiza una consulta que incluye las agendas con sus IDs y los nombres de los doctores
        agendas = Agenda.query.join(Usuario, Usuario.id_u == Agenda.id_doctor).add_columns(
            Agenda.id_a,  # Agrega el ID de la agenda a la consulta
            Agenda.fecha_hora_inicial, 
            Agenda.fecha_hora_final, 
            Usuario.nombre.label('nombre_doctor'),
            Usuario.apellidos.label('apellidos')
        ).all()
        return render_template('agendas.html', agendas=agendas)
    else:
        flash('Debes iniciar sesión para acceder al dashboard', 'warning')
        return render_template('index.html')

@admin.route('/registro_agenda', methods=['GET', 'POST'])
def registro_agenda():
    if request.method == 'POST':
        if session.get('tipo_usuario') == 'admin':
        # Obtener los datos del formulario
         fecha_inicio = request.form['fecha_inicio']
         fecha_fin = request.form['fecha_fin']
         doctor_id = request.form['doctor']  # Esto captura el ID del doctor seleccionado en el formulario

         # Insertar la nueva agenda en la base de datos (debes tener un modelo de datos para las agendas también)
         nueva_agenda = Agenda(fecha_hora_inicial=fecha_inicio, fecha_hora_final=fecha_fin, id_doctor=doctor_id)
         db.session.add(nueva_agenda)
         db.session.commit()

         return render_template('registroagendaexi.html')
        else:
            flash('No tienes permisos para registrar doctores, ni administradores', 'danger')
            return redirect(url_for('index.html'))

    # Si el método es GET, consulta la lista de doctores y muestra el formulario
    doctores = Usuario.query.filter_by(estado_u='activo', rol='doctor').all()
    return render_template('registro_agenda.html', doctores=doctores)
@admin.route('/edita_agenda/<int:id>', methods=['GET', 'POST'])
def edita_agenda(id):

    agenda = Agenda.query.get(id)

    if request.method == 'POST':
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        nuevo_doctor_nombre = request.form['nuevo_doctor']  # Obtén el nuevo nombre del doctor desde el formulario

        # Busca al doctor por nombre en la base de datos
        nuevo_doctor = Usuario.query.filter_by(nombre=nuevo_doctor_nombre, rol='doctor').first()

        if nuevo_doctor:
            # Actualiza los valores de la agenda
            agenda.fecha_hora_inicial = fecha_inicio
            agenda.fecha_hora_final = fecha_fin
            agenda.id_doctor = nuevo_doctor.id_u  # Actualiza el ID del doctor en la agenda

            db.session.commit()

            flash('La agenda se ha actualizado correctamente', 'success')
            return render_template('actuexitag.html')
        else:
            flash('El doctor especificado no existe', 'danger')

    # Consulta la lista de doctores disponibles para llenar el menú desplegable
    doctores = Usuario.query.filter_by(estado_u='activo',rol='doctor').all()

    return render_template('edita_agenda.html', agenda=agenda, doctores=doctores)

    # Lógica para editar información de agendas
    # ...
@admin.route('/eliminar_agenda/<int:id>', methods=['POST'])
def eliminar_agenda(id):
    # Verifica si el usuario actual es un administrador
    if session.get('tipo_usuario') != 'admin':
        flash('No tienes permisos para eliminar agendas', 'danger')
        return redirect(url_for('admin.agendas'))

    # Busca la agenda en la base de datos por su ID
    agenda = Agenda.query.get(id)

    if agenda:
        # Elimina la agenda de la base de datos
        db.session.delete(agenda)
        db.session.commit()
        flash('La agenda ha sido eliminada correctamente', 'success')
        return render_template('eliexitage.html')
    else:
        flash('Agenda no encontrada', 'danger')

    return redirect(url_for('admin.agendas'))

@admin.route('/formulario_modificar/<int:id>', methods=['GET'])
def formulario_modificar(id):
    # Recuperar el objeto producto de la base de datos por su ID
    producto = ProductoAlmacenad.query.get(id)

    if not producto:
        # Manejar el caso donde el producto no se encuentra
        # Puedes mostrar un mensaje de error o redirigir a otra página
        return render_template('error.html', mensaje='Producto no encontrado')

    # Renderizar el formulario de modificación con los datos del producto
    return render_template('actualizar_producto.html', producto=producto)

@admin.route('/actualizar_producto/<int:id>', methods=['POST'])
def actualizar_producto(id):
    # Recuperar el objeto producto de la base de datos por su ID
    producto = ProductoAlmacenad.query.get(id)

    if not producto:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

    # Obtener los nuevos valores desde la solicitud POST
    nuevos_valores = {
        'tipo': request.form.get('tipo', producto.tipo),
        'lente': request.form.get('lente', producto.lente),
        'cantidad': request.form.get('cantidad', producto.cantidad),
    }

    # Actualizar los campos del objeto producto con los nuevos valores
    producto.tipo = nuevos_valores['tipo']
    producto.lente = nuevos_valores['lente']
    producto.cantidad = nuevos_valores['cantidad']

    # Confirmar la actualización en la base de datos
    db.session.commit()

    return render_template('confiractin.html')

@admin.route('/eleccion_citas')
def eleccion_citas():
    return render_template('eleccioncitas.html')
