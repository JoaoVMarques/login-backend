from login_backend.routes.testing_routes import Test_routes
from login_backend.routes.login_routes import Login_routes
from flask import Flask

class Server:
    def __init__(self):
        self.app = Flask('testes')
        self.routes()
        
    def start(self):
        print('servidor iniciado')
        self.app.run()

    def routes(self):
        self.route = Test_routes(self.app)
        self.route = Login_routes(self.app)


if __name__ == '__main__':
    server = Server()
    server.start()