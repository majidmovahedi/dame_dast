from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    UserRegisterSerializer,
    OTPCodeSerializer,
    LoginSerializer,
    UserSerializer,
    NewPasswordSerilizer,
    SendCodeSerilizer,
)
from .helpers import send_sms
from .models import  User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        user = data.save()
        send_sms(user, "register")
        return Response({"status": "ok"})


class UserVerficationView(APIView):
    serializer_class = OTPCodeSerializer

    def post(self, request):
        req_phone_number = request.data.get("phone_number")
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        user = User.objects.get(phone_number=req_phone_number)
        user_dict = user.__dict__
        user_dict["access_token"] = get_tokens_for_user(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserLoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        req_phone_number = request.data.get("phone_number")
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        user = User.objects.get(phone_number=req_phone_number)
        user_dict = user.__dict__
        user_dict["access_token"] = get_tokens_for_user(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
        if not response:
            return Response({"access token not valid "}, status=401)

        user, token = response
        user_dict = user.__dict__
        user_dict["access_token"] = token
        serializer = UserSerializer(user)
        return Response(serializer.data)


class NewPasswordView(APIView):
    serializer_class = NewPasswordSerilizer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        user = data.save()
        return Response({"status": "ok"})


class SendCodeView(APIView):
    serializer_class = SendCodeSerilizer

    def post(self, request):
        req_phone_number = request.data.get("phone_number")
        req_otp_type = request.data.get("otp_type")
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        user = User.objects.get(phone_number=req_phone_number)
        send_sms(user, req_otp_type)

        return Response({"status": "ok"})