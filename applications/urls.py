from django.urls import path
from rest_framework import routers
from . import views


app_name = 'applications'

router = routers.DefaultRouter()
router.register(r'todo', views.TodoView, basename='todo')
urlpatterns = router.urls

urlpatterns += [
    path('speech/', views.SpeechView.as_view(), name='speech'),
    path('podcast/', views.PodcastView.as_view(), name='podcast'),
]