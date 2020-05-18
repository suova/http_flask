import datetime


def test_get_ok(client, data):
    response = client.get("/dictionary/bmstu")
    assert response.status_code == 200
    assert response.data.decode("utf-8").replace("\n",
                                                 "") == '{"result":"nice","time":"%s"}' % datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M")


def test_get_not_exist_key(client, data):
    response = client.get("/dictionary/ok")
    assert response.status_code == 404
    assert response.data.decode("utf-8") == "404 Not Found: Key didn't find"
