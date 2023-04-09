from server import clubs, competitions

class TestUpdatePoints:
    """
    GIVEN : A club secretary wishes to redeem points for a place in a competition
    WHEN : The number of places is confirmed
    THEN : The amount of club points available remain the same
    EXPECTED : The amount of points used should be deducted from the club's balance.
    """

class TestUpdatePoints:
    """
    GIVEN : A club secretary wishes to redeem points for a place in a competition
    WHEN : The number of places is confirmed
    THEN : The amount of club points available remain the same
    EXPECTED : The amount of points used should be deducted from the club's balance.
    """

    def test_update_points(self, client, monkeypatch):
        data = {
            "places": 2,
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }

        monkeypatch.setitem(clubs[0], "points", "13")
        club_points = clubs[0]["points"]

        response = client.post("/purchasePlaces", data=data)

        message = response.data.decode()
        assert response.status_code == 200
        assert clubs[0]["points"] == int(club_points) - data["places"]
        assert "Great-booking complete!" in message
