import pytest
import json
from my_weppy_app import app


@pytest.fixture()
def client():
    return app.test_client()


def test_api_response(client):
    resp = client.get('/api/version')
    resp_json = json.loads(resp.data)
    assert 'status' in resp_json.keys()
    assert 'data' in resp_json.keys()
    assert resp_json['status'] == 'OK'
    assert resp_json['data'].get('version')
