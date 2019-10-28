import os

from django.conf import settings
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from PIL import Image

from .models import *

THUMBNAIL_MAXSIZE = (1024,1024)

#TODO: implement mecanism to remove old files when are changed through admin
#interface

@receiver(post_save, sender=Picture, dispatch_uid='picture_format_generator')
def picture_format_generator(sender,instance, **kwargs):
    print('picture_format_generator')
    image = Image.open(instance.file)

    image_thumb = image.copy()
    image_thumb.thumbnail(THUMBNAIL_MAXSIZE,Image.ANTIALIAS)

    thumb_path = os.path.join( 
            settings.MEDIA_ROOT, 
            settings.MEDIA_IMG_ROOT,
            'thumbs',
            '/'.join(instance.file.name.split('/')[1:-1])
        )

    if not os.path.exists(thumb_path):
        os.makedirs(thumb_path)

    image_thumb.save(
        os.path.join(
            thumb_path,
            instance.file.name.split('/')[-1]
        )
    )


@receiver(pre_save, sender=Picture, dispatch_uid='auto_fill_name')
def auto_fill_name(sender,instance, **kwargs):
    print('auto_fill_name')

    name = instance.file.name.split('/')[-1]
    instance.name = name