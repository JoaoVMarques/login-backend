from login_backend.db import my_db


class Db_queries:
    def selectONE(self, SQL):
        cursor = my_db.cursor()
        cursor.execute(SQL)
        data = cursor.fetchone()
        cursor.reset()

        return data

    def insertOne(self, SQL):
        cursor = my_db.cursor()
        cursor.execute(SQL)
        my_db.commit()
