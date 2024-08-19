from flask import request, render_template, redirect, url_for,session, current_app as app
from datetime import datetime
from business_logic.business import BusinessLogic
from entities.entities import User

user = User()
userLog = None
business_logic = BusinessLogic()
inicio = ''
date = datetime.now().date()


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
        business_logic.crear_user(user=user)
        return render_template('usuariocreado.html', inicio = inicio, date = date)
    except:
        return render_template('errorusuario.html', inicio = inicio, date = date)
    
@app.route('/login', methods = ['POST'])
def submit_login():
    email = request.form.get('email')
    contrasena = request.form.get('contrasena')
    userLog = business_logic.login(email=email,contrasena=contrasena)
    if userLog:
        return render_template('mypage.html', userLog = userLog)
    else:
        return render_template('inicioFallido.html')    
#---------------------------------------------------------------------------
# Paginas esclusivas de usuarios certificados

@app.route('/mypage')
def mypage():
        return render_template('mypage.html', userLog=userLog)

@app.route('/myprofile')
def myprofile():
    return render_template('myprofile.html', userLog=userLog)


@app.route('/agregarempleados')
def agregarEmpleados():
    return render_template('addempleados.html')

@app.route('/empleadocreado')
def empleadoCreado():
    return render_template('empleadocreado.html')

@app.route('/empleadofallido')
def empleadoFallido():
    return render_template('empleadofallido.html')

@app.route('/empleados')
def empleados():
    return render_template('empleados.html')

