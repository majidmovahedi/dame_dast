from django.db import models
from accounts.models import User


# Create your models here.
class Speech(models.Model):
    text_speech = models.CharField(max_length=400)

    def __str__(self):
        return self.text_speech
    

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    media = models.URLField()
    category = models.CharField(max_length=100)
    owener = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    


class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    level = models.IntegerField()                       # 0-1-2 Front dev
    tag = models.CharField(max_length=50)               # Just one Tag Insted Category
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    expire = models.DateTimeField(null=True, blank=True)
    reminder = models.DateTimeField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title