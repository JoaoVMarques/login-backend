from flask import request, jsonify, Response

class Login_routes:
    def __init__(self, app):
        self.app = app
        self.routes()
    
    def routes(self):
        @self.app.route('/login', methods=['POST'])
        def login():
            data = request.json
            if data['email'] == 'teste@email.com' and data['password'] == 'password123':    
                return jsonify(data)
            return {'error': 'email or password not exists'}, 403


