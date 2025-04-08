from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "username": "thundergod", "password": "thundergodpassword"},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "username": "metalgeek", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "username": "zerocool", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "email": "crashoverride@mhigh.edu", "username": "crashoverride", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "username": "sleeptoken", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[2]["_id"], users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Modify the duration field to store total seconds instead of timedelta
        activities = [
            {"_id": ObjectId(), "user_email": "thundergod@mhigh.edu", "activity_type": "Cycling", "duration": int(timedelta(hours=1).total_seconds())},
            {"_id": ObjectId(), "user_email": "metalgeek@mhigh.edu", "activity_type": "Crossfit", "duration": int(timedelta(hours=2).total_seconds())},
            {"_id": ObjectId(), "user_email": "zerocool@mhigh.edu", "activity_type": "Running", "duration": int(timedelta(hours=1, minutes=30).total_seconds())},
            {"_id": ObjectId(), "user_email": "crashoverride@mhigh.edu", "activity_type": "Strength", "duration": int(timedelta(minutes=30).total_seconds())},
            {"_id": ObjectId(), "user_email": "sleeptoken@mhigh.edu", "activity_type": "Swimming", "duration": int(timedelta(hours=1, minutes=15).total_seconds())},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "user_email": "thundergod@mhigh.edu", "score": 100},
            {"_id": ObjectId(), "user_email": "metalgeek@mhigh.edu", "score": 90},
            {"_id": ObjectId(), "user_email": "zerocool@mhigh.edu", "score": 95},
            {"_id": ObjectId(), "user_email": "crashoverride@mhigh.edu", "score": 85},
            {"_id": ObjectId(), "user_email": "sleeptoken@mhigh.edu", "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
