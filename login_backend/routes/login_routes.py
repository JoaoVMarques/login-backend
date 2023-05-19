from flask import request, jsonify
from flask_validate_json import validate_json
from login_backend.routes.schemas.login_schema import schema


class Login_routes:
    def __init__(self, app):
        self.app = app
        self.routes()

    def routes(self):
        @self.app.route('/login', methods=['POST'])
        @validate_json(schema)
        def login():
            data = request.json
            return jsonify(data)
            # email = 'teste@email.com'
            # password = 'password123'
            # if data['email'] == email and data['password'] == password:
            #     return jsonify(data)
            # return {'error': 'email or password not exists'}, 403
