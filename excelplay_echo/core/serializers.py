from rest_framework import serializers
from .models import EchoUser,EchoUserSubmission

class EchoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchoUser
        fields = ('__all__')

class EchoUserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchoUserSubmission
        fields = ('__all__')
