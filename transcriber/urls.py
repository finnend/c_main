from django.urls import path
from .views import upload_audio, stream_audio

app_name = 'transcriber'

urlpatterns = [
    path('upload/', upload_audio, name='upload_audio'),
    path('stream/', stream_audio, name='stream_audio'),
]
