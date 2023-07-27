from flask import Blueprint, render_template
from flask import render_template, request, session, redirect
from app.db import mysql
from data import loadH2SEvets, LoadGoogleEvent
from data import loadH2SEvets, LoadGoogleEvent
import json


main = Blueprint("Main", __name__, template_folder="templates")


# Loading Json Files Of Events

google = LoadGoogleEvent()
Hack2Skill = loadH2SEvets()


all_Events = google + Hack2Skill

featureEvent = [
    {
        "id": "1",
        "path": "static/img/img2.jpg"
    },
    {
        "id": "1",
        "path": "static/img/img1.png"
    }
]

# route of main blueprint start from here


@main.route('/')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'], fe=featureEvent)

    return render_template('home.html', fe=featureEvent)


@main.route('/about')
def about():
    if 'loggedin' in session:
        return render_template('about.html', username=session['username'])

    return render_template('about.html')


@main.route('/contact')
def contact():
    if 'loggedin' in session:
        return render_template('contact.html', username=session['username'])

    return render_template('home.html')


# routes for events pages
@main.route('/events')
def all_events():
    if 'loggedin' in session:
        return render_template('all_events.html',
                               username=session['username'],
                               event=all_Events)
    return render_template('login.html')


@main.route('/past_events')
def outside_event():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM internal_events WHERE is_open=0')
    past_events = cursor.fetchall()

    return render_template('AllEvents.html', past_events=past_events, username=session['username'])


@main.route('/inside_event')
def inside_event():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM internal_events')
        internal_events = cursor.fetchall()

        return render_template('AllEvents.html', username=session['username'],events=internal_events)
    
    return render_template('login.html')


# route for internal hackathons
@main.route('/hackathons')
def hackathon():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM internal_events WHERE tags="hackathon"')
        hk = cursor.fetchall()
        return render_template('hackathon.html',
                               username=session['username'],
                               event=hackathon)

    return render_template('login.html')


@main.route('/online_session')
def sessions():
    if 'loggedin' in session:
        return render_template('AllEvents.html',  username=session['username'])
    return render_template('AllEvents.html')



# routes for authentication register and login
@main.route('/login', methods=['GET', 'POST'])
def login():
    if 'loggedin' in session:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            cursor = mysql.connection.cursor()
            cursor.execute(
                'SELECT * FROM user_register WHERE user_email = %s AND user_password = %s',
                (email, password))

            user = cursor.fetchone()
            print(user)
            if user:
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[1]

                msg = "Successfully login "
                return render_template('home.html',
                                       username=user[0],
                                       session=session, msg=msg)
            else:
                error = "Loggin with correct username and password"
                return render_template('login.html', error=error)
        else:
            return render_template('login.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        # phone_number = request.form['phone']

        try:
            # inserting new user entry into user_register table in database
            cursor = mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO user_register(first_name,last_name,user_email,user_password) VALUES(%s,%s,%s,%s)",
                (fname, lname, email, password))

            cursor.execute(
                "INSERT INTO user_profile(first_name,last_name,user_email) VALUES(%s,%s,%s)",
                (fname, lname, email)
            )
            mysql.connection.commit()
            msg = "Successfully Registered "
            cursor.close()

            # returning template after user is successfully inserted
            return render_template('login.html', msg=msg)
        except Exception as e:
            print(e)
            error = "Please fill form properly"
            return render_template('register.html', error=error, err=e)

    return render_template('register.html')


@main.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect('/login')


# single pages for inside events and hackathon
@main.route('/single_page/<name>', methods=['GET', 'POST'])
def single_page(name):
    if 'loggedin' in session:
        try:
            # fetching event from event table in database
            cursor = mysql.connection.cursor()
            cursor.execute(
                'SELECT * FROM hackathons WHERE event_id= %s', (name))
            hk = cursor.fetchone()

            # rendering template after successfully event is fetch
            return render_template('single_page.html', hack=hk, username=session['username'])

        except Exception as e:
            return render_template('error.html', err=e, username=session['username'])
    else:
        return redirect('/login')


@main.route("/hackathon/user_registration/<name>", methods=['GET', 'POST'])
def user_register(name):
    if 'loggedin' in session:

        if request.method == 'POST':
            tname = request.form['tname']
            lname = request.form['lname']
            m1name = request.form['m1name']
            m2name = request.form['m2name']
            m3name = request.form['m3name']
            m4name = request.form['m4name']
            tech = request.form['tech']
            pname = request.form['pname']

            try:
                # inserting user data into database
                cursor = mysql.connection.cursor()
                cursor.execute('INSERT INTO event_registration(id,team_name, leader_name, memeber1_name,memeber2_name,memeber3_name,memeber4_name,techonology_used,project_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);', (
                    name, tname, lname, m1name, m2name, m3name, m4name, tech, pname))
                mysql.connection.commit()
                msg = "Event Registration Successfull"

                # fetching event from database with event_id
                cursor.execute(
                    'SELECT * FROM hackathons WHERE event_id= %s', (name))
                hk = cursor.fetchone()

                # cursor close
                cursor.close()

                # rendering template after successfully register with message and event
                return render_template('single_page.html', hack=hk, msg=msg, username=session['username'])

            except Exception as e:
                error = "Please Check Value in Fields"
                return render_template('single_page.html', hack=hk, error=error, err=e, username=session['username'])

        return "please Post the request"
    else:
        return redirect('/login')
