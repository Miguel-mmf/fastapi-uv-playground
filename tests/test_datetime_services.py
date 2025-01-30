def test_read_datetime(client):
    response = client.get("/api/v1/datetime")
    assert response.status_code == 200
    assert "current_datetime" in response.json()
