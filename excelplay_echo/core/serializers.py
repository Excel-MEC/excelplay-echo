from rest_framework import serializers
from .models import EchoUser

class EchoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchoUser
        fields = ('__all__')
