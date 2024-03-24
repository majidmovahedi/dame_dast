from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Speech, Podcast, Todo
from .serializers import SpeechSerializer, PodcastSerializer, TodoSerializer


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
    

class TodoView(viewsets.ViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Todo.objects.filter(user_id=request.user)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=self.request.user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)


    def update(self, request, *args, **kwargs):
        instance = Todo.objects.get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        queryset = Todo.objects.get(pk=self.kwargs['pk'])
        queryset.delete()
        return Response({'message': 'todo deleted'})
    