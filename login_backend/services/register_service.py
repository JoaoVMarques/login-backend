from login_backend.utils.db_queries import Db_queries


class Register_service:
    def __init__(self, account):
        self.account = account
        self.query = Db_queries()

    def register(self):
        account = self.account
        sql = f"""INSERT INTO contas (username, password, email) VALUES (
        '{account['username']}',
        '{account['password']}',
        '{account['email']}')"""

        if self.checkAccountValid():
            self.query.insertOne(sql)
            return {'message': 'Conta criada com sucesso!'}

        return {'message': 'O nome de usuário deve ser único'}

    def checkAccountValid(self):
        sql = f"""SELECT username
        FROM contas
        WHERE username = '{self.account['username']}'"""

        account = self.query.selectONE(sql)
        return True if account is None else False
