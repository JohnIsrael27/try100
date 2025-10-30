import json
from app.app import app

def test_home_page():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"Chatbot" in res.data

def test_chat_response():
    client = app.test_client()
    res = client.post("/chat", json={"message": "hello"})
    assert res.status_code == 200
    data = res.get_json()
    assert "reply" in data and isinstance(data["reply"], str)
