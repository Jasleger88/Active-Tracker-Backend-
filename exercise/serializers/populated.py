from .common import ExerciseSerializer
from category.serializers.common import CategorySerializer
# from log.serializers.populated import PopulatedLogSerializer
from jwt_auth.serializers import UserSerializer


class PopulatedExerciseSerializer(ExerciseSerializer):
    category = CategorySerializer()
    # log= PopulatedLogSerializer(many=True)
    owner= UserSerializer()