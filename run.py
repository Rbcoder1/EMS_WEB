from app import create_app
from app.db import mysql

app = create_app()

app.secret_key = "dfdmdsfdzlfld"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'eventmanage'

mysql.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
