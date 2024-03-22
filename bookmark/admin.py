from django.contrib import admin
from . models import Bookmark, UserBookmark, Advertise

# Register your models here.

admin.site.register(Bookmark)
admin.site.register(UserBookmark)
admin.site.register(Advertise)


