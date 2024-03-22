from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Bookmark, UserBookmark, Advertise
from .serializers import BookmarkSerializer, UserBookmarkSerializer, AdsSerializer
#from rest_framework.parsers import FormParser, MultiPartParser


class BookmarkView(APIView):
    serializer_class = BookmarkSerializer

    def get(self, request):
        all_bookmarks = Bookmark.objects.all()
        serializer_data = self.serializer_class(all_bookmarks, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)
  


class UserBookmarkView(viewsets.ViewSet):
    #parser_classes = [MultiPartParser, FormParser]
    serializer_class = UserBookmarkSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = UserBookmark.objects.filter(user_id=request.user)
        serializer = UserBookmarkSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=self.request.user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)


    def update(self, request, *args, **kwargs):
        instance = UserBookmark.objects.get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        queryset = UserBookmark.objects.get(pk=pk)
        queryset.delete()
        return Response({'message': 'bookmark deleted'})
    

    

class AdsView(APIView):
    serializer_class = AdsSerializer

    def get(self, request):
        all_ads = Advertise.objects.all()
        serializer_data = self.serializer_class(all_ads, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)