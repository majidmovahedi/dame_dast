from django.db import models
from django.contrib.auth.models import AbstractUser

 
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    expire_time = models.DateTimeField()
    otp_type = models.CharField(max_length=20)
    active = models.BooleanField(default=False)

