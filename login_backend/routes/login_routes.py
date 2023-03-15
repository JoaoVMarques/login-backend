from flask import request, jsonify


class Login_routes:
    def __init__(self, app):
        self.app = app
        self.routes()

    def routes(self):
        @self.app.route('/login', methods=['POST'])
        def login():
            data = request.json
            email = 'teste@email.com'
            password = 'password123'
            if data['email'] == email and data['password'] == password:
                return jsonify(data)
            return {'error': 'email or password not exists'}, 403
