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
            'image_file': {'required': False, 'max_length': 524288*1024 }
            }


    def validate_image_file(self, image):
        allowed_formats = ['image/png', 'image/jpeg', 'image/jpg', 'image/webp']
        image = self.initial_data.get('image_file')
        if image:
            if image.size > 524288*1024:
                raise serializers.ValidationError("Image file too large ( > 500kb )")
            
            elif image.content_type not in allowed_formats:
                raise serializers.ValidationError("Only PNG & JPG images are allowed.")

            return image

        raise serializers.ValidationError("format not allowed.")



class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = '__all__'
