from server import clubs, competitions
def test_update_points(client):
        data = {
            "places": 2,
            "club": clubs[0]["name"],
            "competition": competitions[0]["name"],
        }
        club_points = clubs[0]["points"]

        response = client.post("/purchasePlaces", data=data)

        message = response.data.decode()
        assert response.status_code == 200
        assert clubs[0]["points"] == int(club_points) - data["places"]
        assert "Great-booking complete!" in message


    

