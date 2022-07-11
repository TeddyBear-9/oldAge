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


class EmpolyeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"
        read_only = [
            'id'
        ]


class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer
        fields = "__all__"
        read_only = [
            'id'
        ]


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
        read_only = [
            'id'
        ]