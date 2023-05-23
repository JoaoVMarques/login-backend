from flask import request
from flask_expects_json import expects_json
from login_backend.routes.schemas.register_schema import schema
from login_backend.services.register_service import Register_service


class Register_routes:
    def __init__(self, app):
        self.app = app
        self.routes()

    def routes(self):
        @self.app.route('/register', methods=['POST'])
        @expects_json(schema, check_formats=True)
        def register():
            service = Register_service
            data = request.json
            response = service.register(data)

            return response
