from flask import Blueprint, render_template, session
from app.db import mysql

user = Blueprint("User", __name__, url_prefix="/user",
                 template_folder="templates")


@user.route('/')
def home():
    username = session['username']
    cursor = mysql.connection.cursor()

    cursor.execute('SELECT * FROM users WHERE fname= %s ', [username])

    user = cursor.fetchone()
    return render_template("profile.html", username=username, user=user)


@user.route('/event_progress')
def event_progress():
    return "event progress"
