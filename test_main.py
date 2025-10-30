from fastapi.testclient import TestClient
from main import app   # lưu ý chạy pytest từ folder chứa main.py

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_hello():
    name = "Dương"
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}"}
