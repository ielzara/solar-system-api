from app.models.planet import Planet
import pytest


def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id=1, name="Saturn", description="Big and ringed", has_moon=True)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Saturn"
    assert result["description"] == "Big and ringed"
    assert result["has_moon"] == True


def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Saturn", description="Big and ringed", has_moon=True)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Saturn"
    assert result["description"] == "Big and ringed"
    assert result["has_moon"] == True


def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1, description="Big and ringed", has_moon=True)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "Big and ringed"
    assert result["has_moon"] == True


def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id=1, name="Saturn", has_moon=True)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Saturn"
    assert result["description"] is None
    assert result["has_moon"] == True


def test_to_dict_missing_has_moon():
    # Arrange
    test_data = Planet(id=1, name="Saturn", description="Big and ringed")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Saturn"
    assert result["description"] == "Big and ringed"
    assert result["has_moon"] is None


def test_from_dict_returns_planet():
    # Arrange
    planet_data = {"name": "Saturn", "description": "Big and ringed", "has_moon": True}

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Saturn"
    assert new_planet.description == "Big and ringed"
    assert new_planet.has_moon == True


def test_from_dict_with_no_name():
    # Arrange
    planet_data = {"description": "Big and ringed", "has_moon": True}

    # Act & Assert
    with pytest.raises(KeyError, match="name"):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_no_description():
    # Arrange
    planet_data = {"name": "Saturn", "has_moon": True}

    # Act & Assert
    with pytest.raises(KeyError, match="description"):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_no_has_moon():
    # Arrange
    planet_data = {"name": "Saturn", "description": "Big and ringed"}

    # Act & Assert
    with pytest.raises(KeyError, match="has_moon"):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "Saturn",
        "description": "Big and ringed",
        "has_moon": True,
        "another": "last value",
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Saturn"
    assert new_planet.description == "Big and ringed"
    assert new_planet.has_moon == True
