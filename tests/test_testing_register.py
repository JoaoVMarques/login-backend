import json
from login_backend.__main__ import Server
from tests.mock.account_register import valid_account


def test_register_route():
    server = Server()
    url = '/register'
    account = json.dumps(valid_account)
    returnMessage = {"message": "Conta criada com sucesso!"}

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = server.app.test_client().post(url, data=account,
                                             headers=headers)
    data = response.data.decode('UTF-8')

    assert (response.status_code == 200)
    assert (returnMessage == json.loads(data))
