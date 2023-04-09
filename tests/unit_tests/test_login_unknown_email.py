from server import clubs, competitions


def test_valid_email(client):
    data = {"email": "john@simplylift.co"}

    response = client.post("/showSummary", data=data)

    assert response.status_code == 200


def test_invalid_email(client):
    data = {"email": "invalid@email.com"}

    response = client.post("/showSummary", data=data)

    message = response.data.decode()
    assert response.status_code == 401
    assert "Sorry, that email was not found." in message


def test_empty_email_field(client):
    data = {"email": " "}

    response = client.post("/showSummary", data=data)

    message = response.data.decode()
    assert response.status_code == 401
    assert "Email field cannot be empty" in message
