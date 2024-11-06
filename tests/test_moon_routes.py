def test_get_all_moons_with_no_records(client):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_moon(client, two_saved_moons):
    # Act
    response = client.get("/moons/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Ocean Moon",
        "description": "watr 4evr",
        "size": 100,
    }


def test_create_one_moon(client):
    # Act
    response = client.post(
        "/moons", json={"name": "New Moon", "description": "The Best!", "size": 150}
    )
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Moon",
        "description": "The Best!",
        "size": 150,
    }


def test_get_all_moons_with_two_records(client, two_saved_moons):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Ocean Moon",
        "description": "watr 4evr",
        "size": 100,
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Desert Moon",
        "description": "so dry",
        "size": 200,
    }


def test_get_all_moons_with_name_query_matching_none(client, two_saved_moons):
    # Act
    data = {"name": "Rocky Moon"}
    response = client.get("/moons", query_string=data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_all_moons_with_name_query_matching_one(client, two_saved_moons):
    # Act
    data = {"name": "Ocean Moon"}
    response = client.get("/moons", query_string=data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "Ocean Moon",
        "description": "watr 4evr",
        "size": 100,
    }


def test_get_one_moon_missing_record(client, two_saved_moons):
    # Act
    response = client.get("/moons/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Moon 3 not found"}


def test_get_one_moon_invalid_id(client, two_saved_moons):
    # Act
    response = client.get("/moons/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Moon cat invalid"}


def test_update_moon(client, two_saved_moons):
    # Arrange
    test_data = {"name": "New Moon", "description": "The Best!", "size": 150}

    # Act
    response = client.put("/moons/1", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": "Moon #1 successfully updated"}


def test_update_moon_with_extra_keys(client, two_saved_moons):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "New Moon",
        "description": "The Best!",
        "size": 150,
        "another": "last value",
    }

    # Act
    response = client.put("/moons/1", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": "Moon #1 successfully updated"}


def test_delete_moon(client, two_saved_moons):
    # Act
    response = client.delete("/moons/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"message": "Moon 1 successfully deleted"}


def test_delete_moon_missing_record(client, two_saved_moons):
    # Act
    response = client.delete("/moons/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Moon 3 not found"}


def test_delete_moon_invalid_id(client, two_saved_moons):
    # Act
    response = client.delete("/moons/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Moon cat invalid"}
