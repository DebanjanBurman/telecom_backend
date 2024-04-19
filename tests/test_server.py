import pytest
import json
from api import app

def test_get_all_customers():
    response = app.test_client().get('/displayCustomer')
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is list
