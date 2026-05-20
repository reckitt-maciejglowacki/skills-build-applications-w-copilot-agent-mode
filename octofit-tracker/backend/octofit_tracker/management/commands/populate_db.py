from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient, ASCENDING

# Sample data for superheroes and teams
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel", "members": ["Iron Man", "Captain America", "Black Widow"]},
    {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
]

ACTIVITIES = [
    {"user": "Superman", "activity": "Flying", "duration": 120},
    {"user": "Iron Man", "activity": "Suit Training", "duration": 90},
    {"user": "Batman", "activity": "Martial Arts", "duration": 60},
]

LEADERBOARD = [
    {"user": "Superman", "points": 300},
    {"user": "Iron Man", "points": 250},
    {"user": "Batman", "points": 200},
]

WORKOUTS = [
    {"name": "Strength Training", "difficulty": "Hard"},
    {"name": "Cardio", "difficulty": "Medium"},
    {"name": "Yoga", "difficulty": "Easy"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', ASCENDING)], unique=True)

        # Insert data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
