from .common import CategorySerializer
from exercise.serializers.common import ExerciseSerializer


class PopulatedCategorySerializer(CategorySerializer):
    exercise = ExerciseSerializer(many=True)