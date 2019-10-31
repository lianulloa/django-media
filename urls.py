from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include
from django.urls import reverse_lazy
from . import views

app_name = 'media'

router = DefaultRouter()
router.register(r'pictures',views.PictureViewSet, base_name='pictures')
router.register(r'videos',views.VideoViewSet, base_name='videos')

urlpatterns = [
    path('',include(router.urls)),
]
