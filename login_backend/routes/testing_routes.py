class Test_routes:
    def __init__(self, app):
        self.app = app
        self.routes()

    def routes(self):
        @self.app.route('/sayhi', methods=['GET'])
        def hello_world():
            return 'Olá mundo!'
