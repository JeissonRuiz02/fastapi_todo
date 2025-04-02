import uuid


def test_register_user(client):
    username = f"testuser_{uuid.uuid4().hex[:6]}"
    response = client.post("/auth/register", json={
        "username": username,
        "password": "testpass"
    })
    assert response.status_code == 201
    assert response.json()["msg"] == "User created successfully"

def test_login_user(client):
    client.post("/auth/register", json={"username": "testuser_login", "password": "testpass"})
    response = client.post("/auth/token", data={"username": "testuser_login", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()