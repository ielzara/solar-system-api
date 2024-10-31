def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act 
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "description": "72368 miles in diameter, a gas giant, red",
        "has_moon": True
    }
def test_create_one_book(client):
    # Act
    response = client.post("/planets", json={
        "id": 1,
        "name": "Saturn",
        "description": "72368 miles in diameter, a gas giant, red",
        "has_moon": True
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "description": "72368 miles in diameter, a gas giant, red",
        "has_moon": True
    }