from django.urls import path
from core.views import Submissionform

urlpatterns =[
    # path('leaderboard',Echoleaderboard.as_view(),name='leaderboard'),
    path('submit',Submissionform,name='finalsubmit')
]
