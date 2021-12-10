from django.contrib import admin
from .models import MessageData, Device

# Register your models here.

@admin.register(MessageData)
class MessageDataAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass