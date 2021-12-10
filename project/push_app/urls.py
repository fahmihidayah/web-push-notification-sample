from django.urls import path
from .apis import AddDeviceView
from .views import send_message_view

urlpatterns = [
    path('api/v1/add_device', AddDeviceView.as_view(), name='api_add_device'),
    path('send_message', send_message_view, name='send_message'),

]