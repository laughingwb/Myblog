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

class CommentAricle(models.Model):
    content_comment = models.TextField(max_length=500)
    user_name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30)
    lifenote = ForeignKey(Lifenote, on_delete=models.CASCADE)

# class Comment(models.Model):
#     content = models.CharField(max_length=500)
#     user_name = models.CharField(max_length=30)
#     time_comment = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
#     lifenote = ForeignKey(Lifenote, on_delete=models.CASCADE)
    # def __str__(self):
    #     return '{1} - {2}'.format(self.user_name,self.Lifenote.title_note)




