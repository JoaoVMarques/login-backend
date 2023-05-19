from flask import make_response, jsonify
from jsonschema import ValidationError


class Error_Handle_Route:
    def __init__(self, app):
        self.app = app
        self.routes()

    def routes(self):
        @self.app.errorhandler(400)
        def bad_request(error):
            if isinstance(error.description, ValidationError):
                print(error)
                original_error = error.description
                return make_response(jsonify(
                    {
                        'error': original_error.message
                    }), 400)
            return error
