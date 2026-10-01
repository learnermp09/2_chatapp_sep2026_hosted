from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_chatgroq():

    response = client.post(
        "/chatgroq/invoke",
        json={"input": {"question": "What is 1+2?"}}
    )

    assert response.status_code == 200

    data = response.json()

    assert "output" in data
    assert data["output"]


def test_openai():

    response = client.post(
        "/chatopenai/invoke",
        json={"input": {"question": "What is 1+2?"}}
    )

    assert response.status_code == 200

    data = response.json()

    assert "output" in data
    assert data["output"]
