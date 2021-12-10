from django.urls import path

from .views import register_token_api, send_message_view


urlpatterns = [
    path('v1/api/register_token', register_token_api, name='register_token'),
    path('fcm/send_message', send_message_view, name='fcm_send_message'),
]