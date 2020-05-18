import datetime


def test_delete_ok(client, data):
    response = client.delete("/dictionary/mail.ru")
    assert response.status_code == 200
    assert response.data.decode("utf-8").replace("\n",
                                                 "") == '{"result":"null","time":"%s"}' % datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M")


def test_delete_not_exist_key(client, data):
    response = client.delete("/dictionary/ok")
    assert response.status_code == 200
    assert response.data.decode("utf-8").replace("\n",
                                                 "") == '{"result":"null","time":"%s"}' % datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M")
