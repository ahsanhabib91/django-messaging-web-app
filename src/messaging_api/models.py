from django.db import models
from django.conf import settings
import time
from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL  # grabing the User model

def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "images/%s.%s" %(int(round(time.time() * 1000)), extension)

def file_upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "files/%s.%s" %(int(round(time.time() * 1000)), extension)

class Message(models.Model):
    msg_sender = models.ForeignKey(User, related_name="sender")
    msg_receiver = models.ForeignKey(User, related_name="receiver")
    message = models.TextField()
    image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True
        )
    file = models.FileField(upload_to=file_upload_location,
            null=True, 
            blank=True
        )
    conversation_id = models.CharField(max_length=120)
    conversation_subject = models.CharField(max_length=120)
    archived = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
