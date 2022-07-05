from django.contrib import admin
from . import models


# Register your models here.

class OldPersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'gender', 'id_card', 'birthday', 'checkin_date', 'checkout_date',
                    'profile_photo', 'room_number', 'firstguardian_name', 'firstguardian_relationship',
                    'firstguardian_phone', 'firstguardian_wechat', 'secondguardian_name',
                    'secondguardian_relationship', 'secondguardian_phone', 'secondguardian_wechat',
                    'health_state', 'description', 'isactive', 'created', 'createby', 'updated',
                    'updateby', 'remove')
    list_filter = ('gender', 'isactive', 'remove', 'created')
    search_fields = ('username', 'room_number')


admin.site.register(models.OldPerson, OldPersonAdmin)
admin.site.register(models.SystemUser)
