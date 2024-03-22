from django.urls import path
from rest_framework import routers
from . import views


app_name = 'bookmark'
router = routers.DefaultRouter()
router.register(r'user_bookmark', views.UserBookmarkView, basename='user_bookmark')
urlpatterns = router.urls

urlpatterns += [
    path('', views.BookmarkView.as_view(), name='bookmark'),
    path('ads/', views.AdsView.as_view(), name='ads'),
]