from datetime import datetime
from django.conf import settings

def generate_upload_path(instance,filename):
    now = datetime.now().strftime('%Y/%b')
    return settings.MEDIA_IMG_ROOT + f'/{now}/{filename}'
