from flask import request, render_template, current_app as app

from bussines import BussinessLogic
from entities import User

business_logic = BussinessLogic()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form['name']
    user = User(name=name)
    result = business_logic.process_user(user)
    return render_template('result.html', result=result)