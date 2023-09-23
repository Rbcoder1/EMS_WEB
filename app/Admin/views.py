from flask import Blueprint, render_template, session,request,redirect
from app.db import mysql

admin = Blueprint("Admin", __name__, url_prefix="/admin",
                  template_folder="./templates")


# login route for admin
@admin.route('/auth',methods=['GET','POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username.lower() == 'imrd' and password.lower() == 'rcp':
            session['admin'] = True
            return redirect('/admin/dash')
        else:
            return redirect('/admin')
    return "Bad Request"


@admin.route('/')
def home():
    if 'admin' in session:    
        cursor = mysql.connection.cursor()
        return render_template('index.html')
    return render_template('Auth.html')


@admin.route('/student')
def student():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_register')
        student = cursor.fetchall()
        return render_template('student.html', student=student)
    return render_template('Auth.html')


@admin.route('/dash')
def dash():
    if 'admin' in session:
        return render_template('dash.html')
    return render_template('Auth.html')


@admin.route('/event_registration')
def hackethon():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM event_registration')
        student = cursor.fetchall()
        return render_template('Event_Regiter.html')
    return render_template('Auth.html')

@admin.route('/user_activity')
def filed_work():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_activity')
        user_act = cursor.fetchall()
        return render_template('User_Activity.html', ua=user_act)
    return render_template('Auth.html')

@admin.route('/allevents')
def fetchevents():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM internal_events')
        allevents = cursor.fetchall()
        return render_template('FetchAllEvents.html',allevents=allevents)
    return render_template('Auth.html')

@admin.route('/fieldwork')
def fieldwork():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM fieldwork')
        fieldw = cursor.fetchall()
        return render_template('fieldwork.html',fieldw=fieldw)
    return render_template('Auth.html')

@admin.route('/feature_banners')
def feature_banner():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM feature_banners')
        fb = cursor.fetchall()
        return render_template('Feature_Banner.html',fb=fb)
    return render_template('Auth.html')

# Insertion route for admin panner
@admin.route('/add_event_page')
def addeventpage():
    if 'admin' in session:
        return render_template('event_add.html')
    return render_template('Auth.html')

@admin.route('add_event_page/add_event',methods=['GET','POST'])
def addevent():
    if 'admin' in session:
        if request.method == 'POST':
            # fetching all values from form
            ename = request.form['ename']
            etag = request.form['etag']
            edesc = request.form['edesc']
            eobj = request.form['eobj']
            erules = request.form['erules']
            etech = request.form['etech']
            ephase = request.form['ephases']
            estatus = request.form['estatus']
            edate = request.form['edate']
            eup = request.form['eup']
            print(ename,etag,edate,edesc,eobj,erules,etech,ephase,estatus,eup)
            # storing in data base 
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO internal_events(event_name,description,tags,images,objective,tech_used,phases,rules,dates,is_open) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ename,edesc,etag,'',eobj,etech,ephase,erules,edate,int(estatus)))
            cursor.connection.commit()
            return "Ok"
        return "cancle"
    return render_template('Auth.html')

@admin.route('/update_event')
def updateevent():
    return "added"

@admin.route('/add_banner')
def addbanner():
    return "added"


