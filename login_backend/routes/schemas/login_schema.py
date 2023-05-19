schema = {
    'type': 'object',
    'properties': {
        'email': {
            'type': 'string',
            'format': 'email',
            'pattern': '^\\S+@\\S+\\.\\S+$',
            "message": {
                "required": "o campo /Email/ é necessário",
                "pattern": "O tipo de email precisa ser valido",
                }
            },
        'password': {
            'type': 'string',
            "message": {
                "required": "o campo /password/ é necessário",
                }
            }
    },
    'required': ['email', 'password']
}
