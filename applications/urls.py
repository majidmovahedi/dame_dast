from django.urls import path
from . import views


app_name = 'applications'

urlpatterns = [
    path('speech/', views.SpeechView.as_view(), name='speech'),
    path('podcast/', views.PodcastView.as_view(), name='podcast'),
]