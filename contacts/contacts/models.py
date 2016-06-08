from django.db import models
import uuid
import os
import time
from ckeditor.fields import RichTextField


def user_directory_path(contact, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'contact', time.strftime("%Y%m%d%H%M") + filename
    ext = filename.split('.')[-1]
    filename_orig = filename.split('.')[0]
    filename = "%s_%s.%s" % (time.strftime("%Y%m%d%H%M"), filename_orig, ext)
    return os.path.join('uploaded_img', filename)


class Contacts(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20, default='SOME STRING')
    image = models.FileField(upload_to=user_directory_path)


class Comments(models.Model):
    f_name = models.ForeignKey(Contacts)
    comment = models.CharField(max_length=200)


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return "-".join([self.username, selfpassword])


class Post(models.Model):
    content = RichTextField()
