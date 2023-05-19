from flask import request, jsonify


class Register_routes:
    def __init__(self, app):
        self.app = app
        self.routes()

    def routes(self):
        @self.app.route('/register', methods=['POST'])
        def register():
            data = request.json
            return jsonify(data)
