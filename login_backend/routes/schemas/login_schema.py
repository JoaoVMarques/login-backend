schema = {
    'type': 'object',
    'properties': {
        'email': {
            'type': 'string',
            'format': 'email',
            },
        'password': {
            'type': 'string',
            }
    },
    'required': ['email', 'password']
}
