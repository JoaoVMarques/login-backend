from login_backend.db import db_cursor, my_db


class Register_service:
    def register(data):
        sql = f"""INSERT INTO contas (username, password, email) VALUES (
        '{data['username']}',
        '{data['password']}',
        '{data['email']}')"""

        db_cursor().execute(sql)
        my_db.commit()
        return {'message': 'Conta criada com sucesso!'}
