from django.db import models

# Create your models here.


class Device(models.Model):

    token = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)


class MessageData(models.Model):

    title = models.CharField(max_length=255)

    message = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)