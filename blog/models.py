from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid
import os
import time


# Create your models here.

def user_directory_path(filename):
    # file will be uploaded to MEDIA_ROOT/uploaded_img
    # return 'contact', time.strftime(wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"%Y%m%d%H%M") + filename
    ext = filename.split('.')[-1]
    filename_orig = filename.split('.')[0]
    filename = "%s_%s.%s" % (time.strftime("%Y%m%d%H%M"), filename_orig, ext)
    return os.path.join('uploaded_img', filename)


class Bloger(models.Model):
    user_id = models.OneToOneField(User, primary_key=True)
    designation = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    img = models.FileField(upload_to=user_directory_path,)


class Blog(models.Model):
    content = RichTextField()
