from server import clubs, competitions


class TestBooking:
    """
    Integration Test
    Test Booking
    """

    def test_booking_places_success(self, client, monkeypatch):
        # Get the home page
        response = client.get("/")
        assert response.status_code == 200

        # Connect to the app
        data_email = {"email": "john@simplylift.co"}
        response_connection = client.post("/showSummary", data=data_email)
        assert response_connection.status_code == 200

        # Book places with a valid competition
        data_book_places = {
            "places": 8,
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }
        monkeypatch.setitem(clubs[0], "points", "13")
        monkeypatch.setitem(competitions[0], "numberOfPlaces", "25")
        monkeypatch.setitem(competitions[0], "date", "2024-03-27 10:00:00")
        response_book_places = client.post("/purchasePlaces", data=data_book_places)
        message = response_book_places.data.decode()
        assert response_book_places.status_code == 200
        assert "Great-booking complete!" in message
