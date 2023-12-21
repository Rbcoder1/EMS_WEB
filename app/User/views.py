from flask import Blueprint, render_template, session, redirect, request
from app.db import mysql
from app.Main import allevent_len
import requests
from serpapi import GoogleSearch
from flask_socketio import join_room,leave_room,send,SocketIO
import app

# Creating a Blueprint for user and its related routes 
user = Blueprint("User", __name__, url_prefix="/user", template_folder="templates")

@user.route('/')
def home():
    if 'loggedin' in session:
        id = session['id']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_register WHERE user_id = %s', [id])
        user_register = cursor.fetchone()
        cursor.execute(
            'SELECT * FROM user_profile WHERE profile_id = %s', [id])
        user_profile = cursor.fetchone()

        if(user_profile != "None" and user_register != "None") :
            user = user_profile + user_register
        profileHealth = 100

        for i in user:
            print(i)
            if i == '' or i == None:
                profileHealth -= 12.5

        return render_template("profile.html", user=user, ph=profileHealth,username=session['username'])
    else:
        return redirect('/login')


@user.route('/progress')
def user_progress():
    # fetching all events counting
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT count(event_id) FROM internal_events')
    internal_event_count = cursor.fetchall()
    allevents = allevent_len() + internal_event_count[0][0]

    # fetching user participation in events
    cursor.execute(
        'SELECT * FROM event_registration WHERE user_id=%s', [session['id']])
    user_register_data = cursor.fetchall()
    user_register_count = len(user_register_data)

    user_progres_data = {
        "total_events": allevents,
        "user_participated": user_register_count,
        "user_missed": allevents - user_register_count,
        "portfolio": int(user_register_count/allevents*100)
    }
    return render_template('progress.html', pdata=user_progres_data,username=session['username'])


@user.route('/job')
def job():
    try:
        params = {
        "engine": "google_jobs",
        "q": "india",
        "hl": "en",
        "api_key": "25f356d132750d01b7b1c531209efc065322bba1e8df57197a7d0fd0bb585eeb",
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        jobs_results = results["jobs_results"]
        return render_template('job.html',jobs=jobs_results)
    except Exception as e:
        error = "Sorrry Job Section Temporary Down"
        return render_template('job.html', error=error,username=session['username'])


@user.route('/learning')
def user_learning():
    return render_template('userlearning.html',username=session['username'])

@user.route('/recent')
def user_recent():
    return render_template('recent.html',username=session['username'])


@user.route('/profile/update', methods=['GET', 'POST'])
def user_update():

    if request.method == 'POST':
        # fetching values from request.form
        first_name = request.form['fname']
        last_nmae = request.form['lname']
        email = request.form['email']
        birthdate = request.form['bdate']
        interest = request.form['interest']
        mobile = request.form['mobile']
        skills = request.form['skills']
        about = request.form['about']
        fgoal = request.form['fgoal']
        userid = session['id']
        photo = request.form['file']

        # storign it in database
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(
                'UPDATE user_profile SET photo=%s,mobile_no=%s,about=%s,b_date=%s,interest=%s,skill=%s,future_goal=%s WHERE profile_id=%s',
                (photo, mobile, about, birthdate, interest, skills, fgoal, userid))
            mysql.connection.commit()
            cursor.close()
            return redirect('/user')
        except Exception as e :
            return "<h1> Fail To Update Server Problem </h1>"
    else:
        return "<h1>Invalid Request</h1>"

# @user.route('/help-room')
# def help_room():
#     socketio = SocketIO(app,cors_allowed_origins="*",async_mode=None)
    

#     return "Help Room"