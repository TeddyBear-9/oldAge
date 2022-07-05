from django.db.models import Min
from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions
"""
id', 'username', 'gender', 'id_card', 'birthday', 'checkin_date', 'checkout_date',
'profile_photo', 'room_number', 'firstguardian_name', 'firstguardian_relationship',
'firstguardian_phone', 'firstguardian_wechat', 'secondguardian_name',
'secondguardian_relationship', 'secondguardian_phone', 'secondguardian_wechat',
'health_state', 'description', 'isactive', 'created', 'createby', 'updated',
'updateby', 'remove'
"""


class OldPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = OldPerson
        fields = "__all__"
        read_only = [
            'id'
        ]

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     """
#     自定义登录认证，使用自有用户表
#     """
#     username_field = 'username'
#
#     def validate(self, attrs):
#         authenticate_kwargs = {self.username_field: attrs[self.username_field], 'password': attrs['password']}
#         print(authenticate_kwargs)
#         try:
#             user = SystemUser.objects.get(**authenticate_kwargs)
#         except Exception as e:
#             raise exceptions.NotFound(e.args[0])
#
#         refresh = self.get_token(user)
#
#         data = {"userId": user.id, "token": str(refresh.access_token), "refresh": str(refresh)}
#         return data

