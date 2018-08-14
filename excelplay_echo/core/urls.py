from django.urls import path
from core.views import Echoleaderboard,Submissionform

urlpatterns =[
    path('leaderboard',Echoleaderboard.as_view()),
    path('submit',Submissionform.as_view())
]
