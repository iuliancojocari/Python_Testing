def test_book_more_than_twelve_places(client):
    club = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}

    competition = {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25",
    }

    data = {"places": 13, "club": club["name"], "competition": competition["name"]}

    response = client.post("/purchasePlaces", data=data)

    message = response.data.decode()
    assert response.status_code == 400
    assert "You cannot book more than 12 places !" in message


def test_book_less_than_twelve_places(client):
    club = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}

    competition = {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25",
    }

    data = {"places": 8, "club": club["name"], "competition": competition["name"]}

    response = client.post("/purchasePlaces", data=data)

    message = response.data.decode()
    assert response.status_code == 200
    assert "Great-booking complete!" in message


def test_empty_field(client):
    club = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}

    competition = {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25",
    }

    data = {"places": " ", "club": club["name"], "competition": competition["name"]}

    response = client.post("/purchasePlaces", data=data)

    message = response.data.decode()
    assert response.status_code == 400
    assert "The field cannot be empty !" in message


def test_book_more_places_than_available(client):
    club = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}

    competition = {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "28",
    }

    data = {"places": 29, "club": club["name"], "competition": competition["name"]}

    response = client.post("/purchasePlaces", data=data)

    message = response.data.decode()
    assert response.status_code == 400
    assert "Number of places unavailable !" in message
