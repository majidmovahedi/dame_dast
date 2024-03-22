from django.db import models

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