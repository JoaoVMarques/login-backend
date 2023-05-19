schema = {
    'type': 'object',
    'properties': {
        'email': {
            'type': 'string',
            'format': 'email',
            },
        'username': {'type': 'string'},
        'password': {
            'type': 'string',
            'minLength': 6,
            'maxLength': 20
            }
    },
    'required': ['email', 'password']
}
