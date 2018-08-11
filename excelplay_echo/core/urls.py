from django.urls import path
from core.views import Echoleaderboard

urlpatterns =[
    path('leaderboard',Echoleaderboard.as_view()),
]
