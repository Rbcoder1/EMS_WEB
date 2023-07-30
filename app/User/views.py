from flask import Blueprint, render_template, session, redirect, request
from app.db import mysql
from app.Main import allevent_len

user = Blueprint("User", __name__, url_prefix="/user",
                 template_folder="templates")

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

        user = user_profile + user_register
        
        profileHealth = 100

        for i in user:
            if i is '':
                profileHealth -= 10

        return render_template("profile.html", user=user, ph=profileHealth)
    else:
        return redirect('/login')


@user.route('/progress')
def user_progress():
    # fetching all events counting
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT count(event_id) FROM internal_events')
    internal_event_count = cursor.fetchall()
    allevents = allevent_len()  + internal_event_count[0][0]

    # fetching user participation in events 

    cursor.execute('SELECT * FROM event_registration WHERE user_id=%s',[session['id']])
    user_register_data = cursor.fetchall();
    user_register_count = len(user_register_data)

    user_progres_data={
        "total_events": allevents,
        "user_participated" : user_register_count,
        "user_missed": allevents - user_register_count,
        "portfolio" : int(user_register_count/allevents*100)  
    }
    return render_template('progress.html', pdata = user_progres_data)


@user.route('/learning')
def user_learning():
    return render_template('userlearning.html')


@user.route('/recent')
def user_recent():
    return render_template('recent.html')


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
        cursor = mysql.connection.cursor()

        cursor.execute(
            'UPDATE user_profile SET photo=%s,mobile_no=%s,about=%s,b_date=%s,interest=%s,skill=%s,future_goal=%s WHERE profile_id=%s',
            (photo, int(mobile), about, birthdate, interest, skills, fgoal, userid))

        mysql.connection.commit()
        cursor.close()
        return redirect('/user')
    else:
        return "<h1>Invalid Request</h1>"
