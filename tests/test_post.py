import datetime


def test_post_ok(client):
    response = client.post("/dictionary", json={"key": "delivery", "value": "awesome"})
    assert response.status_code == 201
    assert response.data.decode("utf-8").replace("\n",
                                                 "") == '{"result":"awesome","time":"%s"}' % datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M")


def test_post_wrong_args(client):
    response = client.post("/dictionary", json={"wrong": "mail.ru", "value": "awesome"})
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "400 Bad Request: Missing param or too much params"


def test_post_more_args(client):
    response = client.post("/dictionary", json={"key": "mail.ru", "wrong": "mail.ru", "value": "awesome"})
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "400 Bad Request: Missing param or too much params"


def test_post_exist_key(client, data):
    response = client.post("/dictionary", json={"key": "mail.ru", "value": "pretty"})
    assert response.status_code == 409
    assert response.data.decode("utf-8") == "409 Conflict: Key already exists"


# check if request is not a json
def test_post_not_json(client, data):
    response = client.post("/dictionary", data={"key": "mail.ru", "value": "pretty"})
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "400 Bad Request: Wrong json"
