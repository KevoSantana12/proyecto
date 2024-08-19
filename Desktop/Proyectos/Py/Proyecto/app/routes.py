from flask import request, render_template, redirect, url_for,session, current_app as app, send_file
from datetime import datetime
from business_logic.user_logica import User_logica
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from business_logic.empleados_logica import Empleado_logica
from entities.entities import User, Empleado
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

user = User()
empleado = Empleado()
userLog = None
business_logic_user = User_logica()
business_logic_empleado = Empleado_logica()
inicio = ''
date = datetime.now().date()

class User(UserMixin):
    def __init__(self, id=None, nombre=None, apellido=None, compania=None, telefono=None, email=None, contrasena=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena
        self.compania = compania
        self.telefono = telefono

#---------------------------------------------------------------------------
#Paginas a las que los usuarios tiene acceso sin registrarse 
@app.route('/')
def home():
    inicio = True
    return render_template('index.html', inicio = inicio, date = date)

@app.route('/inicio')
def inicio():
    inicio = False
    return render_template('inicio.html', inicio = inicio, date = date)

@app.route('/registrese')
def registrese():
    inicio = False
    return render_template('registrese.html', inicio = inicio, date = date)

@app.route('/entrada')
def entrada():
    inicio = False
    return render_template('entrada.html', inicio = inicio, date = date)

@app.route('/nosotros')
def nosotros():
    inicio = False
    return render_template('nosotros.html', inicio = inicio, date = date)

@app.route('/contactenos')
def contactenos():
    inicio = False
    return render_template('contactenos.html', inicio = inicio, date = date)

@app.route('/submit', methods = ['POST'])
def submit_user():
    inicio = False
    user.nombre = request.form.get('nombre')
    user.apellido = request.form.get('apellido')
    user.email = request.form.get('email')
    user.compania = request.form.get('compania')
    user.telefono = request.form.get('telefono')
    user.contrasena = request.form.get('confirmPassword')
    try:
        business_logic_user.crear_user(user=user)
        return render_template('usuariocreado.html', inicio = inicio, date = date)
    except:
        return render_template('errorusuario.html', inicio = inicio, date = date)
    
@app.route('/login', methods = ['POST','GET'])
def submit_login():
    email = request.form.get('email')
    contrasena = request.form.get('contrasena')
    userLog = business_logic_user.login(email=email,contrasena=contrasena)
    if userLog:
        session['id'] = userLog.id
        return redirect(url_for('mypage'))
    else:
        return render_template('inicioFallido.html')    
    
#---------------------------------------------------------------------------
# Paginas esclusivas de usuarios logeados


@login_manager.user_loader
def load_user(user_id):
    return business_logic_user.get_user(int(user_id))

@app.route('/mypage')
def mypage():
    if 'id' not in session:
        return redirect(url_for('login'))
    userLog = business_logic_user.get_user(session['id'])
    sumaSalarioEmpleados = business_logic_empleado.sumaSalarios(session['id'])
    cantidadEmpleados = business_logic_empleado.cantidad_empleados(session['id'])
        
    return render_template('mypage.html', userLog=userLog, sumaSalarioEmpleados=sumaSalarioEmpleados, cantidadEmpleados=cantidadEmpleados)

@app.route('/myprofile', methods=['GET', 'POST'])
def myprofile():
    user_id = session['id']
    userLog = business_logic_user.get_user(user_id)
    if request.method == 'POST':
        try:
            # Obtén los datos del formulario
            nombre = request.form.get('nombre')
            apellido = request.form.get('apellido')
            compania = request.form.get('compania')
            telefono = request.form.get('telefono')
            email = request.form.get('email')
            # contrasena_actual = request.form.get('contrasena_actual')
            # nueva_contrasena = request.form.get('nueva_contrasena')
            # repetir_contrasena = request.form.get('repetir_contrasena')

            # Actualiza los atributos del usuario
            if nombre:
                userLog.nombre = nombre
            if apellido:
                userLog.apellido = apellido
            if compania:
                userLog.compania = compania
            if telefono:
                userLog.telefono = telefono
            if email:
                userLog.email = email

            business_logic_user.update_user(userEditado=userLog, id=user_id)

            return redirect(url_for('myprofile'))
        except Exception as e:
            print(f"Error al actualizar el perfil: {e}")
            return redirect(url_for('error'))

    return render_template('myprofile.html', userLog=userLog)


@app.route('/agregarempleados', methods=['GET', 'POST'])
def agregarEmpleados():
    userLog = business_logic_user.get_user(session['id'])

    if request.method == 'POST':
        empleado.nombre = request.form.get('nombre')
        empleado.apellido = request.form.get('apellido')
        empleado.email = request.form.get('email')
        empleado.telefono = request.form.get('telefono')
        empleado.salarioBruto = request.form.get('salario')
        empleado.posicion = request.form.get('posicion')
        empleado.userId = session['id']
        try:
            business_logic_empleado.crear_empleado(empleado=empleado)
            return render_template('empleadocreado.html', userLog=userLog)
        except:
            return render_template('empleadofallido.html', userLog=userLog)
    else:
        return render_template('addempleados.html', userLog=userLog)

@app.route('/empleadocreado')
def empleadoCreado():
    userLog = business_logic_user.get_user(session['id'])
    return render_template('empleadocreado.html', userLog=userLog)

@app.route('/empleadoeditado')
def empleadoEditado():
    userLog = business_logic_user.get_user(session['id'])
    return render_template('empleadoeditado.html', userLog=userLog)

@app.route('/empleadofallido')
def empleadoFallido():
    userLog = business_logic_user.get_user(session['id'])
    return render_template('empleadofallido.html', userLog = userLog)

@app.route('/empleados')
def empleados():
    userLog = business_logic_user.get_user(session['id'])
    empleados = business_logic_empleado.get_empleados_por_user_id(session['id'])
    return render_template('empleados.html', userLog = userLog, empleados = empleados)


@app.route('/editarempleado/<int:id>', methods=['GET', 'POST'])
def editar_empleado(id):
    empleado = business_logic_empleado.get_empleados_por_id(id)
    userLog = business_logic_user.get_user(session['id'])

    if request.method == 'POST':
        try:
            datos = {
                'nombre': request.form['nombre'],
                'apellido': request.form['apellido'],
                'email': request.form['email'],
                'telefono': request.form['telefono'],
                'salario': float(request.form['salario']),
                'posicion': request.form['posicion'],
                'user_id': userLog.id
            }

            for clave, valor in datos.items():
                setattr(empleado, clave, valor)

            business_logic_empleado.editar_empleado(empleadoeditado=empleado, id=id)

            return render_template('empleadoeditado.html', userLog=userLog)

        except Exception as e:
            print(f"Error al actualizar el empleado: {e}")
            return redirect(url_for('error'))

    return render_template('editarempleado.html', userLog=userLog, empleado=empleado)

@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_empleado(id):
    userLog = business_logic_user.get_user(session['id'])
    business_logic_empleado.borrar_empleado(id=id)
    return render_template('empleadoeliminado.html',  userLog = userLog)

@app.route('/info/<int:id>', methods=['GET', 'POST'])
def info_empleado(id):
    empleado = business_logic_empleado.get_empleados_por_id(id)
    impuesto_renta = business_logic_empleado.impuesto_renta(empleado.salarioBruto)
    ivm = business_logic_empleado.ivm(empleado.salarioBruto)
    sem = business_logic_empleado.sem(empleado.salarioBruto)
    lpt = business_logic_empleado.lpt(empleado.salarioBruto)
    total_impuestos = business_logic_empleado.total_impuestos(empleado.salarioBruto)
    aporte_patronal = business_logic_empleado.aporte_patronal(empleado.salarioBruto)
    salario_neto = business_logic_empleado.salario_neto(empleado.salarioBruto)
    userLog = business_logic_user.get_user(session['id'])

    return render_template('info_empleados.html',  userLog = userLog, 
                           empleado = empleado, impuesto_renta = impuesto_renta, 
                           ivm = ivm, sem = sem, lpt = lpt,
                            aporte_patronal = aporte_patronal, total_impuestos = total_impuestos,
                            salario_neto=salario_neto )


#Creacion de pdfs
@app.route('/descargar_informacion/<int:id>')
def descargar_nomina(id):
        empleado = business_logic_empleado.get_empleados_por_id(id)
        buffer = business_logic_empleado.generar_pdf_nomina(fecha=date, empleado=empleado)
        return send_file(buffer, as_attachment=True, download_name=f'nomina_test.pdf', mimetype='application/pdf')

@app.route('/descargar_empleados')
def descargar_nomina_general():
        userLog = business_logic_user.get_user(session['id'])
        buffer = business_logic_empleado.generar_pdf_planilla_general(id=session['id'], empresa=userLog.compania)
        return send_file(buffer, as_attachment=True, download_name=f'nomina_test.pdf', mimetype='application/pdf')

# @app.route('/delete/<int:empleado_id>', methods=['POST'])
# def deleted_user(empleado_id):
#     empleado_id = request.form['user_id']
#     # result = business_logic.deleteUser(userId)
#     return render_template('deleted.html')



