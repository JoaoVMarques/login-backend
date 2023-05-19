from login_backend.routes.testing_routes import Test_routes
from login_backend.routes.login_routes import Login_routes
from login_backend.routes.error_handle_routes import Error_Handle_Route
from login_backend.routes.register_routes import Register_routes
from flask import Flask


class Server:
    def __init__(self):
        self.app = Flask('testes')
        self.routes()

    def start(self):
        print('servidor iniciado')
        self.app.run()
        self.app.errorhandler(400)

    def routes(self):
        self.route = Error_Handle_Route(self.app)
        self.route = Test_routes(self.app)
        self.route = Login_routes(self.app)
        self.route = Register_routes(self.app)


if __name__ == '__main__':
    server = Server()
    server.start()
