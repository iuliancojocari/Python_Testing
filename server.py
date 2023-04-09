import json
import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    try:
        club = [club for club in clubs if club["email"] == request.form["email"]][0]
        return render_template("welcome.html", club=club, competitions=competitions)
    except IndexError:
        if request.form["email"] == " ":
            flash("Email field cannot be empty")
        else:
            flash("Sorry, that email was not found.")

        return render_template("index.html"), 401


@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]

    date_now = datetime.datetime.now().replace(microsecond=0)
    competition_date = datetime.datetime.strptime(
        foundCompetition["date"], "%Y-%m-%d %H:%M:%S"
    )

    if competition_date >= date_now:
        if foundClub and foundCompetition:
            return render_template(
                "booking.html", club=foundClub, competition=foundCompetition
            )
        else:
            flash("Something went wrong-please try again")
            return render_template("welcome.html", club=club, competitions=competitions)

    flash("You cannot book places in a past competition.")
    return render_template("welcome.html", club=foundClub, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]

    date_now = datetime.datetime.now().replace(microsecond=0)
    competition_date = datetime.datetime.strptime(
        competition["date"], "%Y-%m-%d %H:%M:%S"
    )

    try:
        placesRequired = int(request.form["places"])

        if placesRequired > int(competition["numberOfPlaces"]):
            flash("Number of places unavailable !")
        elif int(club["points"]) < placesRequired:
            flash("Insuficient points !")
        elif placesRequired > 12:
            flash("You cannot book more than 12 places !")
        elif placesRequired > int(competition["numberOfPlaces"]):
            flash("Number of places unavailable !")
        else:
            competition["numberOfPlaces"] = (
                int(competition["numberOfPlaces"]) - placesRequired
            )
            club["points"] = int(club["points"]) - placesRequired
            flash("Great-booking complete!")
            return render_template("welcome.html", club=club, competitions=competitions)

    except ValueError:
        flash("The field cannot be empty !")

    return render_template("booking.html", club=club, competition=competition), 400


# TODO: Add route for points display


@app.route("/logout")
def logout():
    return redirect(url_for("index"))


"""try:

        placesRequired = int(request.form["places"])

        if placesRequired > int(competition["numberOfPlaces"]):
            flash("Number of places unavailable !")
        
        elif placesRequired > 12:
            flash("You cannot book more than 12 places !")

        elif placesRequired > int(club["points"]):
            flash("Insuficient points !")

        elif competition_date < date_now:
            flash("You cannot book places in a past competition.")

        else:
            competition["numberOfPlaces"] = (
                            int(competition["numberOfPlaces"]) - placesRequired
                        )
            club["points"] = int(club["points"]) - placesRequired
            flash("Great-booking complete!")
            return render_template(
                "welcome.html", club=club, competitions=competitions
            )
    
    except ValueError: 
        flash("The field cannot be empty !")

    return render_template("booking.html", club=club, competition=competition), 400"""
