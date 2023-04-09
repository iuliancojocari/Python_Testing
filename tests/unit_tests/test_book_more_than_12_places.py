from server import clubs, competitions


class TestBookingMoreThanTwelvePlaces:
    """
    WHEN : A secretary tries to book more than 12 places in one competition
    THEN : Those places are confirmed
    EXPECTED :
        - They should be able to book no more than 12 places.
        - The UI should prevent them from booking more than 12 places.
        - The places are correctly deducted from the competition.
    """

    def test_book_more_than_twelve_places(self, client, monkeypatch):
        data = {
            "places": 13,
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }

        monkeypatch.setitem(clubs[0], "points", "13")

        response = client.post("/purchasePlaces", data=data)

        message = response.data.decode()
        assert response.status_code == 400
        assert "You cannot book more than 12 places !" in message

    def test_book_less_than_twelve_places(self, client, monkeypatch):
        data = {
            "places": 8,
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }

        monkeypatch.setitem(clubs[0], "points", "15")

        response = client.post("/purchasePlaces", data=data)

        message = response.data.decode()
        assert response.status_code == 200
        assert "Great-booking complete!" in message

    def test_book_more_places_than_available(self, client, monkeypatch):
        data = {
            "places": 6,
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }

        monkeypatch.setitem(competitions[0], "numberOfPlaces", "5")
        monkeypatch.setitem(clubs[0], "points", "8")

        response = client.post("/purchasePlaces", data=data)

        message = response.data.decode()
        assert response.status_code == 400
        assert "Number of places unavailable !" in message

    def test_empty_field(self, client, monkeypatch):
        data = {
            "places": " ",
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }

        monkeypatch.setitem(clubs[0], "points", "15")

        response = client.post("/purchasePlaces", data=data)

        message = response.data.decode()
        assert response.status_code == 400
        assert "The field cannot be empty !" in message