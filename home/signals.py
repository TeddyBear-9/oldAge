from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from .models import Event, SystemUser
from .consumers import send_event
from .serializers import EventSerializer

channel_layer = get_channel_layer()


@receiver(post_init, sender=Event)
def send_notification(sender, **kwargs):
    channel_name = SystemUser.objects.get(pk=2).room_channel_name
    instance = kwargs.get("instance")
    print(instance)
    event_data = EventSerializer(instance).data
    async_to_sync(channel_layer.send)(channel_name,
                                      {"type": "send_event", "event": event_data})
    # send_event(channel_name, event_data)

