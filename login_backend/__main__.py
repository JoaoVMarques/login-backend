from flask import Flask
from login_backend.routes.testing_routes import Test_routes

class Server:
    def __init__(self):
        self.app = Flask('testes')
        self.route = Test_routes(self.app)
        
    def start(self):
        print('servidor iniciado')
        self.app.run()

    def get(self, route):
        return self.app.get(route)

if __name__ == '__main__':
    server = Server()
    server.start()