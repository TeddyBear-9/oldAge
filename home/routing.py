# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/demo/$', consumers.BotConsumer.as_asgi()),
    re_path(r'ws/face_reg/$', consumers.FaceRegConsumer.as_asgi()),
]