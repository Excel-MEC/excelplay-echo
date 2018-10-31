from rest_framework import serializers
from .models import EchoUser,EchoUserSubmission,Problems

class EchoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchoUser
        fields = ('__all__')

class EchoUserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchoUserSubmission
        fields = ('__all__')

class ProbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = ('__all__')

