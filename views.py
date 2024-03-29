from django.shortcuts import render
from .serializers import *
from .models import *

from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import generics, mixins,status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    parser_classes = (FormParser, MultiPartParser)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = SocialVideo.objects.all()
    serializer_class = SocialVideoSerializer
    parser_classes = (FormParser, MultiPartParser)


