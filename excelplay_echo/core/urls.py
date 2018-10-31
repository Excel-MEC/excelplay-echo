from django.urls import path
from core.views import Submissionform,Problem,handshake

urlpatterns =[
    # path('leaderboard',Echoleaderboard.as_view(),name='leaderboard'),
    path('submit',Submissionform,name='finalsubmit'),
    path('probs',Problem,name='Problems'),
    path('handshake',handshake,name='handshake')
]
