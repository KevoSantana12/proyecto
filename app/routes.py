from flask import request, render_template, redirect, url_for, current_app as app
from datetime import datetime
# from business import BusinessLogic
# from entities import User


# business_logic = BusinessLogic()

inicio = ''
date = datetime.now().date()

@app.route('/')
def home():
    inicio = True
    return render_template('index.html', inicio = inicio, date = date)

