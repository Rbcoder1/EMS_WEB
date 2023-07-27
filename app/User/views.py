from flask import Blueprint, render_template, session,redirect
from app.db import mysql

user = Blueprint("User", __name__, url_prefix="/user",
                 template_folder="templates")

profileHealth = 100


@user.route('/')
def home():
    if 'loggedin' in session:
        username = session['username']
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * FROM user_profile WHERE first_name= %s ', [username])

        user = cursor.fetchone()
        return render_template("profile.html", username=username, user=user, ph=profileHealth)
    else:
        return redirect('/login')


@user.route('/progress')
def user_progress():
    return render_template('progress.html')


@user.route('/learning')
def user_learning():
    return render_template('userlearning.html')


@user.route('/recent')
def user_recent():
    return render_template('recent.html')
