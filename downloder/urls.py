from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='inddex'),
    path('download-video/', views.download_youtube_video, name='download_video'),


]
