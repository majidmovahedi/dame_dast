from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User ,OTP
from import_export.admin import ImportExportModelAdmin


class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    pass

admin.site.register(User, CustomUserAdmin)
admin.site.register(OTP)