from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from core.models import EchoUser,EchoUserSubmission,Problems
from core.serializers import EchoUserSerializer,EchoUserSubmissionSerializer,ProbsSerializer
from core.decorators import is_logged_in

from redis_leaderboard.wrapper import RedisLeaderboard
from .judge import run

rdb = RedisLeaderboard('redis',6379,0)

# class Echoleaderboard(APIView):
#     def get(self,request,format=None):
#         leaderboard = EchoUser.objects.all()
#         serializer = EchoUserSerializer(leaderboard,many=True)
#         return Response(serializer.data)

@is_logged_in
def Submissionform(request):
    if request.method=="POST":
        try:
            loginuser = request.session['user']
           
            pid = euser.objects.get(pid=euser.pid)
            eid = EchoUserSubmission.objects.get_or_create(user_id=euser.user_id)
            # fid = EchoUserSubmission.get(fid=eid.fid)

            a = EchoUserSubmissionSerializer()
            if    a.is_valid():
                print(a.data)
                val_out =    a.validated_data
                problem_id = val_out['pid']
                file_id = val_out['val_out']
                
                if(run(problem_id,file_id) == "AC"):
                    pid +=1
                    rdb.add('echo',loginuser,pid)
                    return JsonResponse({'answer':'Correct'})
                else:
                    return JsonResponse({'answer':'Wrong'})


        except Exception as e:
            resp = {'Error': 'Internal Server Error'}
            return JsonResponse(resp, status=500)

def Problem(request):
    if request.method == "GET":
        loginuser = request.session['user']
        euser,created = EchoUser.objects.get_or_create(user_id=loginuser)

        if created:
            rdb.add('echo',loginuser,1)
        level = Problems.objects.filter(pid=euser.pid)[0]
        serializer = ProbsSerializer(level)
        return Response(serializer.data)
      
        

# class Submissionform(generics.CreateAPIView):
#     queryset = EchoUserSubmission.objects.all()
#     serializer_class = EchoUserSubmissionSerializer

#     def post(self,request):
        
#         # user = request.session['user']
#         # euser = EchoUser.objects.get_or_create(user_id=user)
#         # print(euser)
#         # if(run(queryset['pid'],queryset['files'])=="WC"):
#         #     pid += 1
#         return Response(EchoUserSubmissionSerializer.data)