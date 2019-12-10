from django.contrib import admin
from .models import *

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ( 'name','file','created_at','updated_at')
    exclude = ('name',)

# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ( 'name','file','background_image','created_at','updated_at')
#     exclude = ('name',)

@admin.register(SocialVideo)
class SocialVideoAdmin(admin.ModelAdmin):
    list_display = ( 'name','url','created_at','updated_at')
    # exclude = ('name',)
