from flask import request, render_template, redirect, url_for, current_app as app
from datetime import datetime
# from business import BusinessLogic
# from entities import User


# business_logic = BusinessLogic()

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


#---------------------------------------------------------------------------
# Paginas esclusivas de usuarios certificados

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

@app.route('/myprofile')
def myprofile():
    return render_template('myprofile.html')

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

