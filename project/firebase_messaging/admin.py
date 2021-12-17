from django.contrib import admin
from .models import DeviceToken
# Register your models here.

@admin.register(DeviceToken)
class DeviceAdmin(admin.ModelAdmin):
    pass