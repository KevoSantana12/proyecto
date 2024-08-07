from flask import request, render_template, redirect, url_for, current_app as app
from datetime import datetime
# from business import BusinessLogic
# from entities import User


# business_logic = BusinessLogic()

inicio = ''
date = datetime.now().date()

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

@app.route('/mypage')
def mypage():
    inicio = False
    return render_template('mypage.html', inicio = inicio, date = date)

@app.route('/myprofile')
def myprofile():
    inicio = False
    return render_template('myprofile.html', inicio = inicio, date = date)


