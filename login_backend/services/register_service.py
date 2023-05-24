from login_backend.db import my_db


class Register_service:
    def __init__(self, account):
        self.account = account

    def register(self):
        account = self.account
        cursor = my_db.cursor()
        sql = f"""INSERT INTO contas (username, password, email) VALUES (
        '{account['username']}',
        '{account['password']}',
        '{account['email']}')"""

        valid = self.checkAccountValid()
        if valid:
            cursor.execute(sql)
            my_db.commit()
            return {'message': 'Conta criada com sucesso!'}

        return {'message': 'O nome de usuário deve ser único'}

    def checkAccountValid(self):
        sql = f"""SELECT username
        FROM contas
        WHERE username = '{self.account['username']}'"""
        cursor = my_db.cursor()

        cursor.execute(sql)
        account = cursor.fetchone()
        cursor.reset()
        return True if account is None else False
