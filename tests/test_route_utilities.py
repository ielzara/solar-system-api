from app.routes.route_utilities import (
    validate_model,
    create_model,
    get_models_with_filters,
)

from werkzeug.exceptions import HTTPException
from app.models.moon import Moon
from app.models.planet import Planet
import pytest


# We use the `client` fixture because we need an
# application context to work with the database session
def test_create_model_moon(client):
    # Arrange
    test_data = {"name": "New Moon", "size": 124, "description": "The Best!"}

    # Act
    result = create_model(Moon, test_data)

    # Assert
    assert result.status_code == 201
    assert result.get_json() == {
        "id": 1,
        "name": "New Moon",
        "size": 124,
        "description": "The Best!",
    }


def test_create_model_moon_missing_data(client):
    # Arrange
    test_data = {"description": "The Best!"}

    # Act & Assert
    # Calling `create_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached
    with pytest.raises(HTTPException) as error:
        result_moon = create_model(Moon, test_data)

    response = error.value.response
    assert response.status == "400 BAD REQUEST"


def test_create_model_planet(client):
    test_data = {
        "name": "New Planet",
        "description": "A new planet",
        "has_moon": False
    }

    # Act
    result = create_model(Planet, test_data)

    # Assert
    assert result.status_code == 201
    assert result.get_json() == {
        "id": 1, 
        "name": "New Planet",
        "description": "A new planet",
        "has_moon": False
    }


def test_get_models_with_filters_one_matching_moon(two_saved_moons):
    # Act
    result = get_models_with_filters(Moon, {"name": "ocean"})

    # Assert
    assert result == [{"id": 1, "name": "Ocean Moon", "size": 100, "description": "watr 4evr"}]
