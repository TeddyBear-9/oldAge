# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from . import tasks
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import SystemUser, OldPerson, Volunteer, Employee
COMMANDS = {
    'help': {
        'help': '命令帮助信息.',
    },
    'add': {
        'args': 2,
        'help': '计算两个数之和, 例子: `add 12 32`.',
        'task': 'add'
    },
}

channel_layer = get_channel_layer()
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        base64 = text_data_json['message']
        self.send(text_data=json.dumps({
            'base64': base64
        }))


class BotConsumer(WebsocketConsumer):
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        response_message = '请输入`help`获取命令帮助信息。'
        message_parts = message.split()
        if message_parts:
            command = message_parts[0].lower()
            if command == 'help':
                response_message = '支持的命令有:\n' + '\n'.join(
                    [f'{command} - {params["help"]} ' for command, params in COMMANDS.items()])
            elif command in COMMANDS:
                if len(message_parts[1:]) != COMMANDS[command]['args']:
                    response_message = f'命令`{command}`参数错误，请重新输入.'
                else:
                    getattr(tasks, COMMANDS[command]['task']).delay(self.channel_name, *message_parts[1:])
                    response_message = f'收到`{message}`任务.'

        async_to_sync(self.channel_layer.send)(
            self.channel_name,
            {
                'type': 'chat.message',
                'message': response_message
            }
        )

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': f'[机器人]: {message}'
        }))


# 检测的人员类型
person_type_list = [
    'old_people',
    'volunteer',
    'employee',
]


class FaceRegConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        try:
            base64_arr = text_data_json['base64']
            user_id = text_data_json['uid']
            person_id = text_data_json['pid']
            person_type = text_data_json['type']
            user = SystemUser.objects.get(pk=user_id)
            user.face_channel_name = self.channel_name
            user.save()
            if person_type in person_type_list:
                getattr(tasks, "face_reg").delay(self.channel_name, person_id, person_type, base64_arr)

            else:
                self.send(text_data=json.dumps({
                    'message': '请向开发人员确定人员类型是否填写正确'
                }))

        except KeyError:
            self.send(text_data=json.dumps({
                'message': 'id, type, base64 are expected'
            }))

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': f'{message}'
        }))


class RoomEventConsumer(WebsocketConsumer):
    def connect(self):
        user = SystemUser.objects.get(pk=2)
        user.room_channel_name = self.channel_name
        user.save()
        self.accept()

    def disconnect(self, close_code):
        user = SystemUser.objects.get(pk=2)
        user.room_channel_name = None
        user.save()
        pass

    def receive(self, text_data=None, bytes_data=None):

        # Send message to WebSocket
        self.send(text_data=text_data)

    def send_event(self, event):
        event_data = event['event']
        if event_data is None:
            event_data = "empty event"

        self.send(text_data=json.dumps({
            'event_info': event_data
        }))


def send_event(channel_name, event_data):
    async_to_sync(channel_layer.send)(channel_name,
                                      {"type": "send_event", "event": event_data})
