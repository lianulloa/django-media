from django.db import models
from django.conf import settings
from .helpers import generate_img_upload_path, generate_video_upload_path
import os

# Create your models here.
class Picture(models.Model):
    name = models.CharField(blank=True, max_length=100)
    file = models.ImageField(upload_to=generate_img_upload_path, default='img/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'

    def __str__(self):
        return self.file.name


class Video(models.Model):
    name = models.CharField(blank=True, max_length=100)
    file = models.FileField(upload_to=generate_video_upload_path)
    duration = models.DurationField(blank=True)
    background_image = models.ForeignKey(Picture,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Video'
        verbose_name_plural='Videos'

    def __str__(self):
        return self.file.name
