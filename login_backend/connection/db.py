import mysql.connector


my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='login_backend_dev'
)


def db_cursor():
    return my_db.cursor()
