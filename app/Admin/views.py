from flask import Blueprint, render_template

admin = Blueprint("Admin", __name__,url_prefix="/admin",template_folder="./templates")

@admin.route('/')
def home():
    return render_template('index.html')

@admin.route('/student')
def student():
    return render_template('student.html')

@admin.route('/dash')
def dash():
    return render_template('dash.html')

@admin.route('/hackethon')
def hackethon():
    return render_template('hackethon.html')

@admin.route('/filed')
def filed_work(): 
    return render_template('filed_work.html')

