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
def test_create_one_planet(client):
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

def test_update_planet(client, two_saved_planets):
    # Arrange
    test_data = {"name": "New Planet", "description": "The Best!", "has_moon": False}

    # Act
    response = client.put("/planets/1", json=test_data)

    # Assert
    assert response.status_code == 204
  


def test_update_planet_with_extra_keys(client, two_saved_planets):
    # Arrange
    test_data = {
        "id": 1,
        "name": "Saturn",
        "description": "72368 miles in diameter, a gas giant, red",
        "has_moon": True
    }

    # Act
    response = client.put("/planets/1", json=test_data)

    # Assert
    assert response.status_code == 204


def test_update_planet_missing_record(client, two_saved_planets):
    # Arrange
    test_data = {
        "id": 1,
        "name": "Saturn",
        "description": "72368 miles in diameter, a gas giant, red",
        "has_moon": True
    }

    # Act
    response = client.put("/planets/3", json=test_data)

    # Assert
    assert response.status_code == 404


def test_update_planet_invalid_id(client, two_saved_planets):
    # Arrange
    test_data = {
        "id": 1,
        "name": "Saturn",
        "description": "72368 miles in diameter, a gas giant, red",
        "has_moon": True
    }

    # Act
    response = client.put("/planets/cat", json=test_data)

    # Assert
    assert response.status_code == 400


def test_delete_planet(client, two_saved_planets):
    # Act
    response = client.delete("/planets/1")

    # Assert
    assert response.status_code == 204

def test_delete_planet_missing_record(client, two_saved_planets):
    # Act
    response = client.delete("/planets/3")

    # Assert
    assert response.status_code == 404


def test_delete_planet_invalid_id(client, two_saved_planets):
    # Act
    response = client.delete("/planets/3")

    # Assert
    assert response.status_code == 404