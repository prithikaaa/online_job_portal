from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)
class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")

    def __str__(self) :
        return self.title
class Jobs(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=100, null=False, blank=False)
    companyimage = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    skillset = models.TextField(max_length=200, null=False, blank=False)
    def __str__(self) :
        return self.title