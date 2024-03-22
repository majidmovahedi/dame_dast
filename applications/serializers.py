from rest_framework import serializers
from .models import Speech, Podcast

class SpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech
        fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'