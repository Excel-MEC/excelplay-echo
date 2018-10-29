from django.shortcuts import render
from core.models import EchoUser,EchoUserSubmission
from core.serializers import EchoUserSerializer,EchoUserSubmissionSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from redis_leaderboard.wrapper import RedisLeaderboard

rdb = RedisLeaderboard('redis',6380,0)

class Echoleaderboard(APIView):
    def get(self,request,format=None):
        leaderboard = EchoUser.objects.all()
        serializer = EchoUserSerializer(leaderboard,many=True)
        return Response(serializer.data)

class Submissionform(generics.CreateAPIView):
    # user = request.session['user']
    # euser = EchoUser.objects.get_or_create(user_id=user)
    queryset = EchoUserSubmission.objects.all()
    serializer_class = EchoUserSubmissionSerializer

    def handshake(self,request):
        queryset = self.get_queryset()
        user = request.session['user']
        euser = EchoUser.objects.get_or_create(user_id=user)
        