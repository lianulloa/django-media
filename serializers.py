from rest_framework import serializers
from django.urls import reverse
from .models import *

class PictureSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="file.url")
    thumb_url = serializers.SerializerMethodField()

    def get_thumb_url(self,instance):
        url = instance.file.url.split('/')
        return '/' + '/'.join(url[1:3]) + '/thumbs/' + '/'.join(url[3:])

    class Meta:
        model = Picture
        fields = ('id','url','thumb_url')

class VideoSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="file.url")
    background_image = PictureSerializer(read_only=True)
    class Meta:
        model = Video
        fields = ('id','url','background_image')
