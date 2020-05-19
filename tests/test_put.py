import datetime


def test_put_change_ok(client, data):
    response = client.put("/dictionary/mail.ru", json={"key": "mail.ru", "value": "pretty"})
    assert response.status_code == 200
    assert response.data.decode("utf-8").replace("\n",
                                                 "") == '{"result":"pretty","time":"%s"}' % datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M")


def test_put_not_exist_key(client, data):
    response = client.put("/dictionary/vk", json={"key": "vk", "value": "pretty"})
    assert response.status_code == 404
    assert response.data.decode("utf-8") == "404 Not Found: Key didn't find"


def test_put_wrong_args(client, data):
    response = client.put("/dictionary/mail.ru", json={"wrong": "mail.ru", "value": "awesome"})
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "400 Bad Request: Missing param or too much params"


def test_put_more_args(client, data):
    response = client.put("/dictionary/mail.ru", json={"key": "mail.ru", "wrong": "mail.ru", "value": "awesome"})
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "400 Bad Request: Missing param or too much params"


# check if request is not a json
def test_put_not_json(client, data):
    response = client.put("/dictionary/mail.ru", data={"key": "mail.ru", "value": "pretty"})
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "400 Bad Request: Wrong json"
