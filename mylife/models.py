from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Aricletype(models.Model):
    type_name = models.CharField(max_length=30)
    number = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.type_name

class Lifenote(models.Model):
    aricletype = ForeignKey(Aricletype, on_delete=models.CASCADE)
    title_note = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000)
    praisecount = models.IntegerField(default=0)
    def __str__(self):
        return self.title_note

class CommentAricle(models.Model):
    content_comment = models.TextField(max_length=500)
    user_name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30)
    lifenote = ForeignKey(Lifenote, on_delete=models.CASCADE)
    parentcomment = models.ForeignKey('CommentAricle', blank=True, null=True, related_name='p_comment')







