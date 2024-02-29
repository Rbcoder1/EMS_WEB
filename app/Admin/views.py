from flask import Blueprint, render_template, session,request,redirect,Response
from app.db import mysql
from werkzeug.utils import secure_filename
import os
import csv
import io

admin = Blueprint("Admin", __name__, url_prefix="/admin",
                  template_folder="./templates")


UPLOAD_FOLDER = "/home/eventmsystem/mysite/app/static/uploads"

# Routes for Authentication
@admin.route('/login',methods=['GET','POST'])
def loginAdmin():
    if request.method == 'POST':
        token = request.form['token']
        password = request.form['password']
        try:
            if token.strip() == "admin" and password.strip() == "admin@123":
                session['admin'] = True
                print("LoggedIn")
                return redirect("/admin")
            else:
                return render_template("Error.html",error="Internal Server Error")

        except Exception as e:
            print("Internal Server Error", e)

    return "Bad Request"

# main routes 
@admin.route('/')
def home():
    if 'admin' in session:
        print(session)
        return render_template('index.html')
    return render_template('LoginAdmin.html')


@admin.route('/student',methods=['GET','POST'])
def student():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        if request.method == 'POST':
            filtername = request.form['filtername']
            cursor.execute(f"SELECT * FROM user_register ORDER BY {filtername}")
            student = cursor.fetchall();
            return render_template('student.html',student=student)
        else:
            cursor.execute('SELECT * FROM user_register')
            student = cursor.fetchall()
            return render_template('student.html', student=student)
    return render_template('LoginAdmin.html')

@admin.route('/student/ban-student/<id>',methods=['GET','POST'])
def ban_student(id):
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE user_register SET ban=true WHERE user_id=%s",[id])
        cursor.connection.commit()
        
        return {
            "msg": "student ban successfully"
        }
    else:
        return render_template("Error.html")

@admin.route('/dash')
def dash():
    if 'admin' in session:
        return render_template('dash.html')
    return redirect('/auth/login')


@admin.route('/event_registration')
def hackethon():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM event_registration')
        edata = cursor.fetchall()
        return render_template('Event_Regiter.html',edata=edata)
    return render_template('LoginAdmin.html')

@admin.route('/management_event_registration')
def management_event_registration():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM management_event_registrations')
        data = cursor.fetchall()
        
        return render_template('Management_register.html',data=data)
    return render_template('LoginAdmin.html')

@admin.route('/user_activity')
def filed_work():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_activity')
        user_act = cursor.fetchall()
        return render_template('User_Activity.html', ua=user_act)
    return render_template('LoginAdmin.html')

@admin.route('/allevents')
def fetchevents():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM imrdcompetion')
        allevents = cursor.fetchall()
        return render_template('FetchAllEvents.html',allevents=allevents)
    return render_template('LoginAdmin.html')

@admin.route('/fieldwork')
def fieldwork():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM fieldwork')
        fieldw = cursor.fetchall()
        return render_template('fieldwork.html',fieldw=fieldw)
    return render_template('LoginAdmin.html')

@admin.route('/feature_banners')
def feature_banner():
    if 'admin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM feature_banners')
        fb = cursor.fetchall()
        return render_template('Feature_Banner.html',fb=fb)
    return render_template('LoginAdmin.html')


# Routes for Event
# route for add event page
@admin.route('/add_event_page')
def addeventpage():
    if 'admin' in session:
        return render_template('event_add.html')
    return render_template('LoginAdmin.html')

# route for add event in database
@admin.route('add_event_page/add_event',methods=['GET','POST'])
def addevent():
    if 'admin' in session:
        if request.method == 'POST':
            # fetching all values from form
            ename = request.form['ename']
            emode = request.form['emode']
            edesc = request.form['edesc']
            ecat = request.form['ecategory']
            eobj = request.form['eobj']
            erules = request.form['erules'] 
            ementor = request.form['ementor']
            ephase = request.form['ephases']
            edates = request.form['edates']
            ecriteria = request.form['ecriteria']
            eprices = request.form['eprice']
            registration_start_date = request.form['erdate']
            registration_end_date = request.form['eredate']
            event_start_date = request.form['ecdate']
            event_end_date = request.form['ecedate']
            thumbimg = request.form['thumbimg']
            logoimg = request.form['logoimg']
            
            print(thumbimg)
            # storing in data base
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO imrdcompetion(title,description,category,logo_image,thumbnail,mode,objective,rules,\
                           mentors,phases,prices,criteria,dates,registration_start_on,registration_ends_on,event_start_on,event_ends_on)\
                           VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ename,edesc,ecat,thumbimg,logoimg,emode,eobj,erules,ementor,ephase,eprices,\
                            ecriteria,edates,registration_start_date,registration_end_date,event_start_date,event_end_date))
            cursor.connection.commit()
            return redirect('/admin')
        return "cancle"
    return render_template('LoginAdmin.html')

# route for update event in database
@admin.route('/update_event')
def update_event():
    return "updated"

# route for end event by admin
@admin.route('/end_event')
def end_event():
    return "added"

# Routes for Bootcamps Section
# adding a bootcamp in database by admin
@admin.route('/bootcamp/add',methods=['GET','POST'])
def add_bootcamp():
    if 'admin' in session:
        if request.method == "POST":

            title = request.form['title']
            description = request.form['description']
            objective = request.form['objective']
            mode = request.form['mode']
            instructor = request.form['instructor']
            outcome = request.form['outcome']
            hours_per_day = request.form['hours_per_day']
            total_duration = request.form['total_duration']
            cover_image = request.files['cover_image']
            register_start_on = request.form['register_start_on']
            register_end_on = request.form['register_end_on']
            camp_start_on = request.form['camp_start_on']
            camp_end_on = request.form['camp_end_on']

            try:
                if (title and mode and instructor and outcome and total_duration and camp_start_on) == None :
                    return render_template("Error.html", error="Field Are Required")

                # storing file in local
                if cover_image:
                    if cover_image.filename != '':
                        cover_image_name = secure_filename(cover_image.filename)
                        cover_image.save(os.path.join(UPLOAD_FOLDER,cover_image_name))
                        new_cover_image_name = os.path.join(UPLOAD_FOLDER,cover_image_name)
                        print(new_cover_image_name)
                    else :
                        return render_template("Error.html",error="No Image Found")
                else:
                    return render_template("Error.html", error="Please Insert Image [jpg,png] only")


                # uploading image on cloudinary
                # if cover_image:
                #     upload_result = cloudinary.uploader.upload(new_cover_image_name)
                # else:
                #     return render_template("Error.html",error="Problem In Uploading Images")

                # if upload_result :
                #     cover_image_url = upload_result['url']


                # store data in database
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO bootcamps(title,description,objective,mode,instructor,outcome,
                            hours_per_day,total_duration,cover_image,register_start_on,register_end_on,
                            camp_start_on,camp_end_on) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                            (title,description,objective,mode,instructor,outcome,hours_per_day,total_duration,new_cover_image_name,
                                register_start_on,register_end_on,camp_start_on,camp_end_on))
                mysql.connection.commit()

                # seding response back
                return redirect('/admin')
            except Exception as e:
                return render_template("Error.html", error= e)
        else:
            return render_template("bootcamp_add.html")
    else:
        return render_template("Error.html",error="Unauthorized Access")


# updating a bootcamp in database by admin
@admin.route('/bootcamp/update')
def update_bootcamp():
    pass

# delete bootcamp from database
@admin.route('bootcamp/delete/<bootcamp_id>',methods=['GET','POST'])
def delete_bootcamp(bootcamp_id):
    if 'admin' in session:
        if request.method == "POST":
            try :
                # fetch specific bootcamp from batabase & delete it
                cursor = mysql.connection.cursor()
                cursor.execute("DELETE FROM bootcamps WHERE bootcamp_id=%s",[bootcamp_id])
                mysql.connection.commit()
            except Exception as e:
                return render_template("Error.html", error=e)

            return redirect("/admin")
        else:
            return render_template("Error.html", error="Invalid Request")
    else:
        return render_template("Error.html", error="Unauthorized User")

# show all bootcamp with query
@admin.route('bootcamp/fetch/<query>')
def fetch_bootcamp(query):
    if 'username' or 'admin' in session:
        try:
            if query != "None":
                # fetching bootcamps from database
                cursor = mysql.connection.cursor()
                cursor.execute("SELECT * FROM bootcamps WHERE mode=%s",[query])
                specific_bootcamps = cursor.fetchall()
                return render_template("bootcamps.html", bootcamp=specific_bootcamps)
            else:
                # fetching bootcamps from database
                cursor = mysql.connection.cursor()
                cursor.execute("SELECT * FROM bootcamps")
                bootcamps = cursor.fetchall()
                return render_template("bootcamps.html", bootcamps=bootcamps)
        except Exception as e:
            return render_template("Error.html", error=e)
    else:
        return render_template("Error.html", error="Inaccessible Without Login")


@admin.route('/event_registration/report')
def download_report():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM event_registration')
    data = cursor.fetchall()

    output = io.StringIO()
    writer = csv.writer(output)

    line = ['register_id','roll_no','topic','tech_used','team_name','leader_name','member1_name','member2_name','member3_name','member4_name','register_at','user_id','event_name']
    writer.writerow(line)

    for row in data:
        line = [str(row[0]) + ',' + str(row[1]) + ',' + str(row[2])  + ',' +  str(row[3]) + ',' + str(row[4]) + ',' + str(row[5]) + ',' + str(row[6]) + ',' + str(row[7]) + ',' +  str(row[8]) + ',' + str(row[9]) + ',' + str(row[10]) + ',' + str(row[11]) + ',' + str(row[12])]
        writer.writerow(line)
    
    output.seek(0)

    return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=employee_report.csv"})