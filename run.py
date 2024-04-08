from app import create_app
from app.db import mysql
from dotenv import load_dotenv
import cloudinary
import os

load_dotenv()

app = create_app()

# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "imrdindd_imrdtechclub"
# app.config['MYSQL_PASSWORD'] = "Rcpimrd@123"
# app.config['MYSQL_DB'] = "imrdindd_imrdtechclub"


app.secret_key = "dfdmdsfdzlfld"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "eventmanage"


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
