from app.models.moon import Moon


def test_to_dict_no_missing_data():
    # Arrange
    test_data = Moon(id=1, name="Ocean Moon", description="watr 4evr", size=100)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Ocean Moon"
    assert result["description"] == "watr 4evr"
    assert result["size"] == 100


def test_to_dict_missing_id():
    # Arrange
    test_data = Moon(name="Ocean Moon", description="watr 4evr", size=100)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Ocean Moon"
    assert result["description"] == "watr 4evr"
    assert result["size"] == 100


def test_to_dict_missing_name():
    # Arrange
    test_data = Moon(id=1, description="watr 4evr", size=100)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "watr 4evr"
    assert result["size"] == 100


def test_to_dict_missing_description():
    # Arrange
    test_data = Moon(id=1, name="Ocean Moon", size=100)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Ocean Moon"
    assert result["description"] is None
    assert result["size"] == 100


def test_to_dict_missing_size():
    # Arrange
    test_data = Moon(id=1, name="Ocean Moon", description="watr 4evr")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Ocean Moon"
    assert result["description"] == "watr 4evr"
    assert result["size"] is None
