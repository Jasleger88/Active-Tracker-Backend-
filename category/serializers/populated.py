from shoe.serializers.common import ShoeSerializer
from .common import CategorySerializer


class PopulatedCategorySerializer(CategorySerializer):
    exercise = ExerciseSerializer(many=True)