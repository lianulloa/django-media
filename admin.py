from django.contrib import admin
from .models import *

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ( 'name','file','created_at','updated_at')
    exclude = ('name',)