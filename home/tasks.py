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

    # if instance is None:
    #     print("person type error")
    #     async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": "The person type is illegal"})
    # else:
    #     instance.data = {
    #         'base64': base64_arr
    #     }
    #     print(str(instance) + "is saving")
    #     instance.save()
    #     print("save done")
    #     async_to_sync(channel_layer.send)(channel_name,
    #                                       {"type": "chat.message", "message": "success"})
