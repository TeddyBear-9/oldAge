# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        base64 = text_data_json['message']
        # base64 = text_data['message']
        # print("接受消息:" +
        #       'base64:\n' +
        #       str(base64))
        self.send(text_data=json.dumps({
            'base64': base64
        }))
