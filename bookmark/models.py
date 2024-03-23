from django.db import models
from accounts.models import User
#from django.core.validators import FileExtensionValidator 

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    media = models.TextField()

    def __str__(self):
        return self.title
    


class UserBookmark(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    image_file = models.ImageField(upload_to= '%Y/%m/%d') # , validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg','webp',])]
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Advertise(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    media = models.TextField()
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.title
