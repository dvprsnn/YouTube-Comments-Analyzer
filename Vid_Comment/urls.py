from django.urls import path
from . import views
from .views import CommentData, Video_data, video_form

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('video_data', CommentData.as_view(), name='video_records'),
    path('get_records', Video_data.as_view(), name='get_records'),
    path('form', video_form, name='form'),
]
