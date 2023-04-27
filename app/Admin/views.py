from flask import Blueprint, render_template

admin = Blueprint("Admin", __name__,url_prefix="/admin")


@admin.route('/')
def home():
    return "Admin"
