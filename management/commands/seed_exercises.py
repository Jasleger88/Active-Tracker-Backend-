# seed_exercises.py

from django.core.management.base import BaseCommand
from active_tracker_backend.models import Category, Exercise

class Command(BaseCommand):
    help = 'Seed the database with exercise data'

    def handle(self, *args, **kwargs):
        categories = [
            'Back', 'Arms', 'Legs', 'Shoulders', 'Chest', 'Core'
        ]

        exercises = {
            'Back': [
                {"name": "Pull Up", "description": "An exercise for the upper back and arms."},
                {"name": "Deadlift", "description": "A compound exercise targeting the back and legs."}
            ],
            'Arms': [
                {"name": "Bicep Curl", "description": "An exercise targeting the biceps."},
                {"name": "Tricep Dip", "description": "An exercise for the triceps."}
            ],
            'Legs': [
                {"name": "Squat", "description": "A compound exercise for the legs."},
                {"name": "Lunge", "description": "An exercise targeting the leg muscles."}
            ],
            'Shoulders': [
                {"name": "Shoulder Press", "description": "An exercise for the shoulder muscles."},
                {"name": "Lateral Raise", "description": "An exercise targeting the deltoids."}
            ],
            'Chest': [
                {"name": "Bench Press", "description": "A compound exercise for the chest."},
                {"name": "Push Up", "description": "An exercise targeting the chest muscles."}
            ],
            'Core': [
                {"name": "Bench Press", "description": "A compound exercise for the chest."},
                {"name": "Push Up", "description": "An exercise targeting the chest muscles."}
            ]
        }

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            for exercise_data in exercises[category_name]:
                Exercise.objects.get_or_create(
                    name=exercise_data["name"],
                    description=exercise_data["description"],
                    category=category
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with exercise data'))
