from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from .models import OldPerson, Volunteer, Employee

channel_layer = get_channel_layer()


@shared_task
def add(channel_name, x, y):
    message = '{}+{}={}'.format(x, y, int(x) + int(y))
    async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": message})
    print(message)


@shared_task
def face_reg(channel_name, pid, type, base64_arr):
    instance = None
    print(type)
    if type == 'old_people':
        print('before get')
        instance = OldPerson.objects.get(pk=pid)
        print('after get')
    elif type == 'volunteer':
        instance = Volunteer.objects.get(pk=pid)
    elif type == 'employee':
        instance = Employee.objects.get(pk=pid)

    print(instance)

    if instance is None:
        print("person type error")
        async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": "The person type is illegal"})
    else:
        instance.data = {
            'base64': base64_arr
        }
        print(str(instance) + "is saving")
        instance.save()
        print("save done")
        async_to_sync(channel_layer.send)(channel_name,
                                          {"type": "chat.message", "message": "success"})

# @shared_task
# def search(channel_name, name):
#     spider = PoemSpider(name)
#     result = spider.parse_page()
#     async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": str(result)})
#     print(result)
#
#
# class PoemSpider(object):
#     def __init__(self, keyword):
#         self.keyword = keyword
#         self.url = "https://so.gushiwen.cn/search.aspx"
#
#     def parse_page(self):
#         params = {'value': self.keyword}
#         response = requests.get(self.url, params=params)
#         if response.status_code == 200:
#             # 创建Selector类实例
#             selector = Selector(response.text)
#             # 采用xpath选择器提取诗人介绍
#             intro = selector.xpath('//textarea[starts-with(@id,"txtareAuthor")]/text()').get()
#             print("{}介绍:{}".format(self.keyword, intro))
#             if intro:
#                 return intro
#
#         print("请求失败 status:{}".format(response.status_code))
#         return "未找到诗人介绍。"