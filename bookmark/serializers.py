from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Bookmark, UserBookmark, Advertise


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'



class UserBookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserBookmark
        fields = ('id', 'title', 'link','image_file', 'created', 'user_id')
        read_only_fields = ('user_id',)

        extra_kwargs = {
            'image_file': {'required': False, 'max_length': 105000 }
            }


    def validate_link(self, req_link):
        if UserBookmark.objects.filter(link = req_link).exists():
            raise serializers.ValidationError("this link is already exists")
        return req_link
        

    #100 * 1024
    def validate_image_file(self, image):
        allowed_formats = ['image/png', 'image/jpeg', 'image/jpg', 'image/webp']
        image = self.initial_data.get('image_file')
        if image:
            if image.size > 105000:
                raise serializers.ValidationError("Image file too large ( > 100kb )")
            
            elif image.content_type not in allowed_formats:
                raise serializers.ValidationError("Only PNG & JPG images are allowed.")

            return image

        raise serializers.ValidationError("فرمت فایل پشتیبانی نمی شود.")



class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = '__all__'
