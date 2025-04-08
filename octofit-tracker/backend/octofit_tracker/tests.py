from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId

class OctoFitApiTests(TestCase):
    def setUp(self):
        # Create test client
        self.client = APIClient()
        
        # Create test user
        self.test_user = User.objects.create(
            _id=ObjectId(),
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        
        # Create test team
        self.test_team = Team.objects.create(
            _id=ObjectId(),
            name='Test Team'
        )
        
        # Create test activity
        self.test_activity = Activity.objects.create(
            _id=ObjectId(),
            user=self.test_user,
            activity_type='Running',
            duration=timedelta(minutes=30)
        )
        
        # Create test leaderboard entry
        self.test_leaderboard = Leaderboard.objects.create(
            _id=ObjectId(),
            user=self.test_user,
            score=100
        )
        
        # Create test workout
        self.test_workout = Workout.objects.create(
            _id=ObjectId(),
            name='Test Workout',
            description='A workout for testing'
        )
    
    def test_user_list(self):
        """Test retrieving user list"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
    
    def test_team_list(self):
        """Test retrieving team list"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
    
    def test_activity_list(self):
        """Test retrieving activity list"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
    
    def test_leaderboard_list(self):
        """Test retrieving leaderboard list"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
    
    def test_workout_list(self):
        """Test retrieving workout list"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
