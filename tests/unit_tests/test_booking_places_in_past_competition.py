import datetime
from server import clubs, competitions


def test_booking_places_in_past_competition(client):
    date_now = datetime.datetime.now().replace(microsecond=0)
    competition_date = datetime.datetime.strptime(
        competitions[0]["date"], "%Y-%m-%d %H:%M:%S"
    )

    data = {"places": 1, "club": clubs[0]["name"], "competition": competitions[0]["name"]}

    response = client.post("/purchasePlaces", data=data)

    message = response.data.decode()
    assert competition_date < date_now
    assert response.status_code == 400
    assert "You cannot book places in a past competition." in message

