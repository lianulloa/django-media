from django.db import models
from .helpers import generate_upload_path

# Create your models here.
class Picture(models.Model):
    name = models.CharField(blank=True, max_length=100)
    file = models.ImageField(upload_to=generate_upload_path, default='img/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'

    def __str__(self):
        return self.file.name

    def __unicode__(self):
        return self.file.url
