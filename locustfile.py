from server import clubs, competitions
from locust import HttpUser, task, between

class LocustTestServer(HttpUser):
    wait_time = between(1, 5)
    competition = competitions[0]
    club = clubs[0]

    def on_start(self):
        self.client.get("/", name=".index")
        self.client.post("/showSummary", data={'email': self.club["email"]}, name=".show_summary")

    @task
    def get_booking(self):
        self.client.get(
            f"/book/{self.competition['name']}/{self.club['name']}",
            name="book"
        )

    @task
    def post_booking(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 0,
                "club": self.club["name"],
                "competition": self.competition["name"]
            },
            name="purchase_places"
        )

    @task
    def get_board(self):
        self.client.get("/points", name="view_club_points")