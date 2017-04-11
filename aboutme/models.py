from django.db import models
import os, uuid
from django.db.models.fields.related import ForeignKey

# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('avatar', filename)

class Myself(models.Model):
    user_name = models.CharField(max_length=30)
    introduce = models.CharField(max_length=100)
    content = models. TextField(max_length=500)
    avatar = models.ImageField(upload_to=get_file_path, blank=True)
    qq_number = models.CharField(max_length=30)
    job_post = models.CharField(max_length=30)
    work_time = models.DateField(blank=True, null=True)
    university = models.CharField(max_length=30)
    education_background = models.CharField(max_length=30)

class Technical(models.Model):
    name = models.CharField(max_length=30)
    introduce = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
         return self.name

class UseTechnial(models.Model):
    myself = ForeignKey(Myself, on_delete=models.CASCADE)
    technical = ForeignKey(Technical, on_delete=models.CASCADE)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    def __str__(self):
         return self.technical.name