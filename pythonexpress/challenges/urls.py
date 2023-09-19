from django.urls import path
from . import views

app_name = 'challenges'  

urlpatterns = [
    # URL for the daily challenge page, using a dynamic parameter for challenge_id
    path('challenge/', views.daily_challenge, name='daily_challenge'),

    # URL for the leaderboard page
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    # Add other URLs for your app's views as needed
]
