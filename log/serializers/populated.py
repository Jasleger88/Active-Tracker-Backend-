from .common import LogSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedLogSerializer(LogSerializer):
    owner = UserSerializer()