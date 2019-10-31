from datetime import datetime
from django.conf import settings

def generate_img_upload_path(instance,filename):
    now = datetime.now().strftime('%Y/%b')
    return settings.MEDIA_IMG_ROOT + f'/{now}/{filename}'

def generate_video_upload_path(instance,filename):
    now = datetime.now().strftime('%Y/%b')
    return settings.MEDIA_VIDEO_ROOT + f'/{now}/{filename}'
