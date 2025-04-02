def get_token(client):
    client.post("/auth/register", json={"username": "testuser", "password": "testpass"})
    res = client.post("/auth/token", data={"username": "testuser", "password": "testpass"})
    return res.json()["access_token"]


def test_create_task(client):
    token = get_token(client)
    response = client.post("/tasks/", json={"title": "Test Task"}, headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"

def test_get_tasks(client):
    token = get_token(client)
    response = client.get("/tasks/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
