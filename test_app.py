import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_hello_route(client):
    response = client.get('/')
    assert response.data == b"Hello, DevOps!"