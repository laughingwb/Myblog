from django.db import models
import os, uuid
from django.db.models.fields.related import ForeignKey


class Message(models.Model):
    content = models.TextField(max_length=500)
    person_name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    creat_time = models.CharField(max_length=30)

class ReplyMessage(models.Model):
    message = ForeignKey(Message, on_delete=models.CASCADE)
    reply_name = models.CharField(max_length=30)
    qq_num = models.CharField(max_length=30)
    reply_content = models.TextField(max_length=500)
    creat_time = models.DateTimeField(auto_now_add=True)