def test_use_more_points_than_available(client):
    club = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "8"}

    competition = {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25",
    }

    data = {"places": 15, "club": club["name"], "competition": competition["name"]}

    response = client.post("/purchasePlaces", data=data)

    message = response.data.decode()
    assert response.status_code == 400
    assert "Insuficient points !" in message


def test_use_available_points(client):
    club = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}

    competition = {
        "name": "Spring Festival",
        "date": "2023-04-27 10:01:02",
        "numberOfPlaces": "25",
    }

    data = {"places": 2, "club": club["name"], "competition": competition["name"]}

    response = client.post("/purchasePlaces", data=data)

    message = response.data.decode()
    assert response.status_code == 200
    assert "Great-booking complete!" in message
