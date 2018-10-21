from django.urls import path
from core.views import Echoleaderboard,Submissionform

urlpatterns =[
    path('leaderboard',Echoleaderboard.as_view(),name='leaderboard'),
    path('submit',Submissionform.as_view(),name='finalsubmit')
]
