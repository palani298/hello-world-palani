from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI app!"}

def test_helloworld():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.text == '"Hello World!"'

def test_helloworld_json():
    response = client.get("/helloworld", headers={"Accept": "application/json"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_helloworld_timezone():
    response = client.get("/helloworld?tz=America/New_York", headers={"Accept": "application/json"})
    assert response.status_code == 200
    assert "Hello World! It is" in response.json()["message"]
    assert "America/New_York" in response.json()["message"]

def test_helloworld_invalid_timezone():
    response = client.get("/helloworld?tz=Invalid/Timezone", headers={"Accept": "application/json"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid timezone specified."}

def test_unravel():
    test_data = {
        "key1": {"keyA": ["foo", 0, "bar"]},
        "some other key": 2,
        "finally": "end"
    }
    expected = ["key1", "keyA", "foo", 0, "bar", "some other key", 2, "finally", "end"]
    
    response = client.post("/unravel", json=test_data)
    assert response.status_code == 200
    assert response.json() == expected 