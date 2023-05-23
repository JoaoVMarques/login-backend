from flask import request, jsonify
from flask_expects_json import expects_json
from login_backend.routes.schemas.register_schema import schema
from login_backend.connection.db import db_cursor, my_db


class Register_routes:
    def __init__(self, app):
        self.app = app
        self.routes()

    def routes(self):
        @self.app.route('/register', methods=['POST'])
        @expects_json(schema, check_formats=True)
        def register():
            data = request.json
            sql = f"""INSERT INTO contas (username, password, email) VALUES (
            '{data['username']}',
            '{data['password']}',
            '{data['email']}')"""

            db_cursor().execute(sql)
            my_db.commit()

            return jsonify(data)
