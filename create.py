import os
import csv

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
os.environ['DATABASE_URL'] = "postgresql://postgres:mojoj0j0@localhost:5432/postgres"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    #creates the databases in accordance with models.py
    db.create_all()

    #demonstrating INSERT
    f=open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        #add an entry in the Flight class
        db.session.add(flight)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit()

    #demonstrating SELECT
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()