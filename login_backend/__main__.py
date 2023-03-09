from flask import Flask

class Server:
    def __init__(self):
        self.app = Flask('testes')
        @self.app.route("/sayhi")
        def hello_world():
            return 'Olá mundo!'
        
    def start(self):
        print('servidor iniciado')
        self.app.run()

if __name__ == '__main__':
    server = Server()
    server.start()