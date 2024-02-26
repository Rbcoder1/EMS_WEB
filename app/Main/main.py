from flask import Blueprint, render_template
from flask import render_template, request, session, redirect
from app.db import mysql
from data import loadH2SEvets, LoadGoogleEvent
from data import loadH2SEvets, LoadGoogleEvent

# Creating a Blueprint for main pages
main = Blueprint("Main", __name__, template_folder="templates")

# Loading Json Files Of Events
google = LoadGoogleEvent()
Hack2Skill = loadH2SEvets()

all_Events = google + Hack2Skill
all_Events_length = len(all_Events)


# routes for main pages like home,about,contact,etc
@main.route('/')
def home():
    cursor = mysql.connection.cursor()
    # fetching banner
    cursor.execute('SELECT * FROM feature_banners')
    featureEvent = cursor.fetchall()
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'], fe=featureEvent, allevents=all_Events[0:4])
    else:
        return render_template('home.html', fe=featureEvent, allevents=all_Events[0:4])


@main.route('/about')
def about():
    if 'loggedin' in session:
        return render_template('about.html', username=session['username'])
    return render_template('about.html')


@main.route('/contact')
def contact():
    if 'loggedin' in session:
        return render_template('contact.html', username=session['username'])
    return redirect('/login')


# routes for events pages
@main.route('/events')
def all_events():
    if 'loggedin' in session:
        return render_template('all_events.html',
                               username=session['username'],
                               event=all_Events)
    return redirect('/login')


@main.route('/past_events')
def outside_event():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM internal_events WHERE is_open=0')
    past_events = cursor.fetchall()
    return render_template('AllEvents.html', events=past_events, username=session['username'])


@main.route('/inside_event')
def inside_event():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM internal_events')
        internal_events = cursor.fetchall()
        return render_template('AllEvents.html', username=session['username'], events=list(internal_events))
    return redirect('/login')


# route for different events and category of events
@main.route('/hackathons')
def hackathon():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM internal_events WHERE tags="hackathon" and is_open=1')
        hk = cursor.fetchall()
        print(hk)
        return render_template('hackathon.html', username=session['username'], event=hk)
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
            if user:
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[1]

                return render_template('home.html',
                                       username=user[0],
                                       session=session)
            else:
                error = "Loggin with correct username and password"
                return render_template('Authentication.html', error=error)
        else:
            return render_template('Authentication.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if 'loggedin' in session:
        return redirect('/')
    else:
        if request.method == 'POST':
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            password = request.form['password']
            try:
                cursor = mysql.connection.cursor()
                cursor.execute(
                    "INSERT INTO user_register(first_name,last_name,user_email,user_password) VALUES(%s,%s,%s,%s)",
                    (fname, lname, email, password))
                mysql.connection.commit()
                msg = "Successfully Registered "

                cursor.execute(
                    'SELECT user_id FROM user_register WHERE user_email = %s',
                    [email])
                uid = cursor.fetchone()

                cursor.execute(
                    "INSERT INTO user_profile(profile_id) VALUES(%s)",
                    (uid))

                mysql.connection.commit()
                cursor.close()

                # returning template after user is successfully inserted
                return render_template('Authentication.html')

            except Exception as e:
                # error = "Already Register"
                error = e
                return render_template('Authentication.html', error=error, err=e)

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
                'SELECT * FROM internal_events WHERE event_id= %s', (name))
            hk = cursor.fetchone()

            # rendering template after successfully event is fetch
            return render_template('single_page.html', hack=hk, username=session['username'])

        except Exception as e:
            return render_template('single_page.html', err=e, username=session['username'])
    else:
        return redirect('/login')


@main.route("/hackathon/user_registration/<name>", methods=['GET', 'POST'])
def user_register(name):
    if 'loggedin' in session:
        if request.method == 'POST':
            if 'rno' in request.form:
                rno = request.form['rno']
            if 'topic' in request.form:
                tname = request.form['topic']
            else:
                tname = 'None'
            if 'tech' in request.form:
                tech = request.form['tech']
            else:
                tech = 'None'
            if 'teamname' in request.form:
                teamname = request.form['teamname']
            else:
                teamname = 'None'
            if 'leadname' in request.form:
                leadname = request.form['leadname']
            else:
                leadname = 'None'
            if 'm1name' in request.form:
                m1name = request.form['m1name']
            else:
                m1name = 'None'
            if 'm2name' in request.form:
                m2name = request.form['m2name']
            else:
                m2name = 'None'
            if 'm3name' in request.form:
                m3name = request.form['m3name']
            else:
                m3name = 'None'
            if 'm4name' in request.form:
                m4name = request.form['m4name']
            else:
                m4name = 'None'

            try:
                # inserting user data into database
                cursor = mysql.connection.cursor()
                cursor.execute(
                    'SELECT event_name FROM internal_events WHERE event_id=%s', [name])
                eventname = cursor.fetchone()

                cursor.execute('INSERT INTO event_registration(user_id,event_name,roll_no,topic,tech_used,team_name,leader_name,member1_name,member2_name,member3_name,member4_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', (
                    int(session['id']), eventname, int(rno), tname, tech, teamname, leadname, m1name, m2name, m3name, m4name))
                mysql.connection.commit()
                msg = "Event Registration Successfull"

                # fetching event from database with event_id
                cursor.execute(
                    'SELECT * FROM internal_events WHERE event_id= %s', (name))
                hk = cursor.fetchone()
                cursor.close()

                # rendering template after successfully register with message and event
                return render_template('single_page.html', hack=hk,username=session['username'])

            except Exception as e:
                error = "Please Check Value in Fields"
                return render_template('single_page.html', error=error, err=e, username=session['username'])

        return "please Post the request"
    else:
        return redirect('/login')


@main.route('/learning-path')
def learning_path():
    return render_template('learning-path.html')


@main.route('/roadmaps')
def roadmaps():
    return render_template('roadmap.html')
