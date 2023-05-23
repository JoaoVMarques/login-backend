import json
from login_backend.__main__ import Server
from tests.mock.account_register import valid_account


def test_register_route():
    returnMessage = {"message": "Conta criada com sucesso!"}
    server = Server()
    url = '/register'
    account = json.dumps(valid_account)

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = server.app.test_client().post(url, data=account,
                                             headers=headers)
    data = response.data.decode('UTF-8')

    print(data)
    assert (response.status_code == 200)
    assert (returnMessage == json.loads(data))
