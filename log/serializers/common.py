from rest_framework import serializers
from ..models import Log
# from brand.serializers import CategorySerializer


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
