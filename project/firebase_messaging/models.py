from django.db import models

# Create your models here.


class DeviceToken(models.Model):

    token = models.CharField(max_length=255)

    user_id = models.IntegerField()