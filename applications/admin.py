from django.contrib import admin
from . models import Speech, Podcast, Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
        list_display = ['title', 'user_id', 'created']

admin.site.register(Speech)
admin.site.register(Podcast)
admin.site.register(Todo, TodoAdmin)
