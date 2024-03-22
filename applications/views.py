from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Speech, Podcast
from .serializers import SpeechSerializer, PodcastSerializer


class SpeechView(APIView):
    serializer_class = SpeechSerializer

    def get(self, request):
        all_bookmarks = Speech.objects.all()
        serializer_data = self.serializer_class(all_bookmarks, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)


class PodcastView(APIView):
    serializer_class = PodcastSerializer

    def get(self, request):
        all_bookmarks = Podcast.objects.all()
        serializer_data = self.serializer_class(all_bookmarks, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)