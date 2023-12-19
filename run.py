from app import create_app
from app.db import mysql
from dotenv import load_dotenv
import cloudinary
import os

load_dotenv()

app = create_app()

app.secret_key = os.environ.get("SECRET_KEY")
app.config['MYSQL_HOST'] = os.environ.get("DATABASE_URI")
app.config['MYSQL_USER'] = os.environ.get("DATABASE_USERNAME")
app.config['MYSQL_PASSWORD'] = os.environ.get("DATABASE_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("DATABASE_NAME")

UPLOAD_FOLDER = "app/static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# configuring cloudinary 
config = cloudinary.config(
        cloud_name="dtlapidol",
        api_key="427972763672626",
        api_secret="PcfBwDVucSC4VUsGSTK8LUQ2NT8",
        secure=True
    )

try:
    mysql.init_app(app)
except Exception as e: 
    print("DATABASE CONNECTION FAILED :" ,e)


if __name__ == "__main__":
    app.run(debug=True)
