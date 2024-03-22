from .views import (
    UserRegisterView,
    UserVerficationView,
    UserLoginView,
    UserStatusView,
    NewPasswordView,
    SendCodeView,
)
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainSlidingView

app_name = 'accounts'
urlpatterns = [
    path("register", UserRegisterView.as_view(), name="register"),
    path("verify", UserVerficationView.as_view(), name="verify"),
    path("login", UserLoginView.as_view(), name="login"),
    path("new_password", NewPasswordView.as_view(), name="new_password"),
    path("user_status", UserStatusView.as_view(), name="user_status"),
    path("send_code", SendCodeView.as_view(), name="send_code"),
]
