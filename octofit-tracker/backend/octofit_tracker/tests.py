from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Clark Kent", email="clark@dc.com", team="DC", is_superhero=True)
        self.assertEqual(user.name, "Clark Kent")
        self.assertTrue(user.is_superhero)

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Marvel", description="Marvel Superheroes")
        self.assertEqual(team.name, "Marvel")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name="Bruce Wayne", email="bruce@dc.com", team="DC", is_superhero=True)
        activity = Activity.objects.create(user=user, type="Running", duration=30, calories=300, date="2025-11-21")
        self.assertEqual(activity.type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="DC", description="DC Superheroes")
        leaderboard = Leaderboard.objects.create(team=team, points=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body workout", difficulty="Medium", duration=15)
        self.assertEqual(workout.name, "Pushups")
