class TestLogin:
    """
    WHEN : A user types in an email not found in the system
    THEN : App crashes
    EXPECTED :Code should be written to ensure that if something goes
                wrong (like the email isn't found), the error is caught
                and handled. Display an error message like "Sorry, that
                email wasn't found."
    """

    def test_valid_email(self, client):
        data = {"email": "john@simplylift.co"}

        response = client.post("/showSummary", data=data)

        assert response.status_code == 200

    def test_invalid_email(self, client):
        data = {"email": "invalid@email.com"}

        response = client.post("/showSummary", data=data)

        message = response.data.decode()
        assert response.status_code == 401
        assert "Sorry, that email was not found." in message

    def test_empty_email_field(self, client):
        data = {"email": " "}

        response = client.post("/showSummary", data=data)

        message = response.data.decode()
        assert response.status_code == 401
        assert "Email field cannot be empty" in message