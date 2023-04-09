import datetime
from server import clubs, competitions


class TestBookingPastCompetition:
    """
    GIVEN : A secretary wishes to book a number of places for a competition
    WHEN : They book a number of places on a competition that has happened in the past
    THEN : They receive a confirmation message
    EXPECTED : They should not be able to book a place on a post-dated
                competition (but past competitions should be visible).
    """

    def test_booking_places_in_past_competition_invalid(self, client):
        """
        Test with invalid competition date
        """
        date_now = datetime.datetime.now().replace(microsecond=0)
        competition_date = datetime.datetime.strptime(
            competitions[0]["date"], "%Y-%m-%d %H:%M:%S"
        )

        data = {"club": clubs[0]["name"], "competition": competitions[0]["name"]}

        response = client.get(
            f"/book/{competitions[0]['name']}/{clubs[0]['name']}", data=data
        )

        message = response.data.decode()
        assert competition_date < date_now
        assert response.status_code == 200
        assert "You cannot book places in a past competition." in message

    def test_booking_places_in_past_competition_valid(self, client, monkeypatch):
        """
        Test with valid competition date
        """
        monkeypatch.setitem(competitions[0], "date", "2024-03-27 10:00:00")

        date_now = datetime.datetime.now().replace(microsecond=0)
        competition_date = datetime.datetime.strptime(
            competitions[0]["date"], "%Y-%m-%d %H:%M:%S"
        )

        data = {"club": clubs[0]["name"], "competition": competitions[0]["name"]}

        response = client.get(
            f"/book/{competitions[0]['name']}/{clubs[0]['name']}", data=data
        )

        assert competition_date >= date_now
        assert response.status_code == 200
