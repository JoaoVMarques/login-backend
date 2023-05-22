from login_backend.__main__ import Server


def test_sayhi_route():

    server = Server()
    response = server.app.test_client().get('/sayhi')
    data = response.data.decode('UTF-8')
    assert (response.status_code == 200)
    assert ("Olá mundo!" in data)
