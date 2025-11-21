from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC', is_superhero=True),
            User(name='Batman', email='batman@dc.com', team='DC', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date='2025-11-21')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=450, date='2025-11-21')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=600, date='2025-11-21')
        Activity.objects.create(user=users[3], type='Yoga', duration=20, calories=100, date='2025-11-21')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body workout', difficulty='Medium', duration=15)
        Workout.objects.create(name='Squats', description='Lower body workout', difficulty='Easy', duration=10)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=750, rank=1)
        Leaderboard.objects.create(team=dc, points=700, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
