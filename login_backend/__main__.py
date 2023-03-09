from flask import Flask
from routes.test_routes import Test_routes

class Server:
    def __init__(self):
        self.app = Flask('testes')
        self.route = Test_routes(self.app)
        
    def start(self):
        print('servidor iniciado')
        self.app.run()

if __name__ == '__main__':
    server = Server()
    server.start()