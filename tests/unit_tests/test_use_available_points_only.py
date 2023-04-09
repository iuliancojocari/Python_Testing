from server import clubs, competitions

class TestUseAvailablePoints:
    """
    WHEN : A secretary redeems more points than they have available,
            which would leave them in the negative
    THEN : They receive a confirmation message
    EXPECTED :
        - They should not be able to redeem more points than available;
            this should be done within the UI.
        - The redeemed points should be correctly deducted from the club's total.
    """

    def test_use_available_points(self, client, monkeypatch):
        data = {
            "places": 8,
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }

        monkeypatch.setitem(clubs[0], "points", "13")

        response = client.post("/purchasePlaces", data=data)

        message = response.data.decode()
        assert response.status_code == 200
        assert "Great-booking complete!" in message

    def test_use_more_points_than_available(self, client, monkeypatch):
        data = {
            "places": 6,
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }

        monkeypatch.setitem(clubs[0], "points", "5")

        response = client.post("/purchasePlaces", data=data)

        message = response.data.decode()
        assert response.status_code == 400
        assert "Insuficient points !" in message
