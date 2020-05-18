import pytest

from server import app


@pytest.fixture()
def client():
    client = app.test_client()
    return client


# some methods require initial data
@pytest.fixture()
def data(client):
    client.post("/dictionary", json={"key": "mail.ru", "value": "awesome"})
    client.post("/dictionary", json={"key": "bmstu", "value": "nice"})
