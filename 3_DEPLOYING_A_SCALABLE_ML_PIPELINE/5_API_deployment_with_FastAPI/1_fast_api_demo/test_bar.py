#test_bar.py

import json
from fastapi.testclient import TestClient

from bar import app

client= TestClient(app)

def test_post():
    data = json.dumps({"value": 42})
    response = client.post("/42?query=42", data=data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["path"] == 42
    assert response.json()["query"] == 42
    assert response.json()["body"] == {"value": 42}
