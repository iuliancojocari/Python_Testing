def test_valid_email(client):
    club = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}

    data = {"email": club["email"]}

    response = client.post("/showSummary", data=data)

    assert response.status_code == 200


def test_invalid_email(client):
    club = {"name": "Simply Lift", "email": "invalid@email.com", "points": "13"}

    data = {"email": club["email"]}

    response = client.post("/showSummary", data=data)

    message = response.data.decode()
    assert response.status_code == 401
    assert "Sorry, that email was not found." in message


def test_empty_email_field(client):
    club = {"name": "Simply Lift", "email": "", "points": "13"}

    data = {"email": club["email"]}

    response = client.post("/showSummary", data=data)

    message = response.data.decode()
    assert response.status_code == 401
    assert "Email field cannot be empty" in message
