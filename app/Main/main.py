from flask import Blueprint, render_template
from flask import render_template, request, session, redirect
from app.db import mysql
from data import loadH2SEvets
import datetime


# Creating a Blueprint for main pages
main = Blueprint("Main", __name__, template_folder="templates")

# Loading Json Files Of Events
Hack2Skill = loadH2SEvets()

all_Events = Hack2Skill
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
        return render_template('home.html', fe=featureEvent, allevents=all_Events[0:9])


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
    cursor.execute('SELECT * FROM imrdcompetion WHERE is_open=0')
    past_events = cursor.fetchall()
    return render_template('AllEvents.html', events=past_events, username=session['username'])


@main.route('/inside_event')
def inside_event():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM imrdcompetion')
    imrdcompetion = cursor.fetchall()
    return render_template('AllEvents.html', events=list(imrdcompetion))



# route for different events and category of events
@main.route('/hackathons')
def hackathon():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM imrdcompetion WHERE event_ends_on > %s',[datetime.date.today()])
        hk = cursor.fetchall()
        print(hk)
        return render_template('hackathon.html', username=session['username'], event=hk)
    return render_template('Authentication.html')


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
@main.route('/single_page/<id>', methods=['GET', 'POST'])
def single_page(id):
    # try:
        # fetching event from event table in database
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM imrdcompetion WHERE event_id= %s', [id])
        event = cursor.fetchone()

        cursor.execute('SELECT count(register_id) FROM management_event_registrations WHERE event_id=%s',[id])
        register_count = cursor.fetchall()

        print(register_count)
        return render_template('single_page.html', hack=event, count=register_count,username=session['username'])
    # except Exception as e:
    #     return render_template('single_page.html', err=e)

# event Registration for management activity
@main.route("/events/user_registration/<name>", methods=['GET', 'POST'])
def user_register(name):
    if 'loggedin' in session:
        if request.method == 'POST':
            rno1 = request.form['rno1']
            class1 = request.form['class1']
            mob1 = request.form['mob1']
            memeber1_name = request.form['member1_name']
            rno2 = request.form['rno2']
            class2 = request.form['class2']
            mob2 = request.form['mob2']
            memeber2_name = request.form['member2_name']
            rno3 = request.form['rno3']
            class3 = request.form['class3']
            mob3 = request.form['mob3']

            try:
                # inserting user data into database
                cursor = mysql.connection.cursor()
                cursor.execute('INSERT INTO management_event_registrations(event_id,user_id,roll_no,class,mobile_no,member1_name,member1_rollno,member1_class,member1_mob,member2_name,member2_rollno,member2_class,member2_mob,fees_confirm) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', (
                    name,int(session['id']), int(rno1),class1,mob1,memeber1_name,rno2,class2,mob2,memeber2_name,rno3,class3,mob3,0))
                mysql.connection.commit()
                msg = "Event Registration Successfull"
                return redirect(f'/single_page/{name}')
            
            except Exception as e:
                error = "Please Check Value in Fields"
                return render_template('single_page.html', error=error, err=e, username=session['username'])
        else:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT category,event_id FROM imrdcompetion WHERE event_id=%s",[name])
            category, event_id = cursor.fetchone()

            return render_template("eventRegistration.html", category=category, eventid = event_id ,username=session['username'])
    else:
        return redirect('/login')


@main.route('/learning-path')
def learning_path():
    return render_template('learning-path.html')


@main.route('/roadmaps')
def roadmaps():
    return render_template('roadmap.html')
