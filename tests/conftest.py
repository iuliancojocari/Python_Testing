import pytest
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def valid_competition():
    return {
        "name": "Test Competition",
        "date": "2024-03-27 10:00:00",
        "numberOfPlaces": "25",
    }
