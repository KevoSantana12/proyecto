from flask import request, render_template, redirect, url_for, current_app as app

from business import BusinessLogic
from entities import User


business_logic = BusinessLogic()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def submit():
    name = request.form['name']
    user = User (name = name)

    result = business_logic.process_user(user)
    return render_template ('result.html', result = result)

@app.route('/users')
def users():
    all_users = business_logic.get_all_users()
    return render_template('users.html', users=all_users)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        user = User()
        user.name = request.form['name']
        user.id = request.form['id']
        result = business_logic.update_user(user)
        return redirect(url_for('users'))
    else:
        all_users = business_logic.get_all_users()
        user = next((u for u in all_users if u['id'] == user_id), None)
        return render_template('edit_user.html', user=user) 

@app.route('/delete/<int:user_id>', methods=['POST'])
def deleted_user(user_id):
    userId = request.form['user_id']
    result = business_logic.deleteUser(userId)
    return render_template('deleted.html')

