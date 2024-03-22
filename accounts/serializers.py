from rest_framework import serializers
from .models import User, OTP
from datetime import datetime ,timedelta
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", "password"]

    def validate(self, attrs):
        req_phone_number = attrs.get("phone_number")
        try:
            user = User.objects.get(phone_number=req_phone_number)
            raise serializers.ValidationError("این شماره در سیستم وجود دارد")
        except User.DoesNotExist:
            return super().validate(attrs)
        
    def create(self, validated_data):
        user = User(username=validated_data['phone_number'],phone_number=validated_data['phone_number'],is_active=False)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        req_phone_number = attrs.get("phone_number")
        req_password = attrs.get("password")

        try:
            user = User.objects.get(phone_number=req_phone_number)
            if not user.is_active:
                raise serializers.ValidationError("User Not active!")

            user = authenticate(username=user.username, password=req_password)
            if not user:
                raise serializers.ValidationError("نام کاربری یا رمز عبور اشتباه است!")

        except User.DoesNotExist:
            raise serializers.ValidationError("نام کاربری وجود ندارد")
        return super().validate(attrs)


class OTPCodeSerializer(serializers.Serializer):
    code = serializers.CharField()
    phone_number = serializers.CharField()
    

    def validate_code(self, value):
        req_code = self.initial_data["code"]
        req_phone_number = self.initial_data["phone_number"]

        try:
            user = User.objects.get(phone_number=req_phone_number)
            otp = OTP.objects.get(
                code=req_code,
                user=user.pk,
                expire_time__gt=datetime.now(),
                otp_type="register",
            )
            otp.delete()
            return value
        except OTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or OTP has expired.")
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found !")

    def create(self, validated_data):
        validated_phone_number = validated_data["phone_number"]
        user = User.objects.get(phone_number=validated_phone_number)
        user.is_active = True
        user.save()
        return user


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    access_token = serializers.CharField()



class NewPasswordSerilizer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()
    password = serializers.CharField()

    def validate_code(self, value):
        req_phone_number = self.initial_data["phone_number"]
        req_code = self.initial_data["code"]
        try:
            user = User.objects.get(phone_number=req_phone_number)
            otp = OTP.objects.get(
                code=req_code,
                user=user.pk,
                expire_time__gt=datetime.now(),
                otp_type="forget",
            )
            otp.delete()
            return value
        except OTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or OTP has expired.")
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found !")

    def create(self, validated_data):
        validated_phone_number = validated_data["phone_number"]
        validated_password = validated_data["password"]
        user = User.objects.get(phone_number=validated_phone_number)
        user.set_password(validated_password)
        user.save()
        return user



class SendCodeSerilizer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp_type = serializers.CharField()

    def validate(self, attrs):
        req_phone_number = attrs.get("phone_number")
        req_otp_type = attrs.get("otp_type")
        try:
            user = User.objects.get(phone_number=req_phone_number)
            if req_otp_type == "register":
                if user.is_active:
                    raise serializers.ValidationError("User is Active!")
            otp = OTP.objects.get(
                    user=user.pk,
                    expire_time__gt=datetime.now(),
                    otp_type=req_otp_type,
                )
            if otp:
                raise serializers.ValidationError("2 دقیقه دیگر امتحان کنید.")
        except OTP.DoesNotExist:
            pass
        except User.DoesNotExist:
            raise serializers.ValidationError("User Not Found!")
        return super().validate(attrs)