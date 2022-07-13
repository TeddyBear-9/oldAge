import datetime

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, mixins
from rest_framework_simplejwt import authentication
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView, \
    GenericAPIView, DestroyAPIView, UpdateAPIView
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated


def index(request):
    return render(request, 'chat/index.html', {})


class OldPersonModelView(ModelViewSet):
    queryset = OldPerson.get_all()
    serializer_class = OldPersonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.remove = '已删除'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=False, url_path="statistics")
    def get_statistics(self, request, *args, **kwargs):
        now = datetime.date.today().strftime("%Y-%m-%d")
        old_o80 = OldPerson.get_all().filter(birthday__lt='1942-01-01').count()
        old_y80_o70 = OldPerson.get_all().filter(birthday__gt='1942-01-01', birthday__lt='1952-01-01').count()
        old_y70_o60 = OldPerson.get_all().filter(birthday__gt='1952-01-01', birthday__lt='1962-01-01').count()
        old_y60 = OldPerson.get_all().filter(birthday__gt='1962-01-01').count()
        return Response(data=[old_o80, old_y80_o70, old_y70_o60, old_y60], status=status.HTTP_200_OK)


class EmployeeModelView(ModelViewSet):
    queryset = Employee.get_all()
    serializer_class = EmpolyeeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.remove = '已删除'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=False, url_path="statistics")
    def get_statistics(self, request, *args, **kwargs):
        now = datetime.date.today().strftime("%Y-%m-%d")
        emy_o80 = Employee.get_all().filter(birthday__lt='1942-01-01').count()
        emy_y80_o70 = Employee.get_all().filter(birthday__gt='1942-01-01', birthday__lt='1952-01-01').count()
        emy_y70_o60 = Employee.get_all().filter(birthday__gt='1952-01-01', birthday__lt='1962-01-01').count()
        emy_y60 = Employee.get_all().filter(birthday__gt='1962-01-01').count()
        return Response(data=[emy_o80, emy_y80_o70, emy_y70_o60, emy_y60], status=status.HTTP_200_OK)


class VolunteerModelView(ModelViewSet):
    queryset = Volunteer.get_all()
    serializer_class = VolunteerSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.remove = '已删除'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=False, url_path="statistics")
    def get_statistics(self, request, *args, **kwargs):
        now = datetime.date.today().strftime("%Y-%m-%d")
        vlt_o80 = Volunteer.get_all().filter(birthday__lt='1942-01-01').count()
        vlt_y80_o70 = Volunteer.get_all().filter(birthday__gt='1942-01-01', birthday__lt='1952-01-01').count()
        vlt_y70_o60 = Volunteer.get_all().filter(birthday__gt='1952-01-01', birthday__lt='1962-01-01').count()
        vlt_y60 = Volunteer.get_all().filter(birthday__gt='1962-01-01').count()
        return Response(data=[vlt_o80, vlt_y80_o70, vlt_y70_o60, vlt_y60], status=status.HTTP_200_OK)


class RegisterView(CreateAPIView):
    serializer_class = OldPersonSerializer
    queryset = SystemUser.objects.all()
    authentication_classes = None

    def post(self, request, *args, **kwargs):
        serializers = OldPersonSerializer(data=request.data)

        if not serializers.is_valid(raise_exception=True):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(data=serializers.data, status=status.HTTP_200_OK)


class EventModelView(ModelViewSet):
    queryset = Event.get_all()
    serializer_class = EventSerializer
    permission_classes = []
    authentication_classes = []

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.remove = '已删除'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class GetFaceView(viewsets.GenericViewSet,
#                   mixins.ListModelMixin):
#
#     permission_classes = [AllowAny]
#     authentication_classes = []
#     serializer_class = ImgSerializer
#
#     def list(self, request, *args, **kwargs):
#         old = OldPerson.get_all()
#         vlt = Volunteer.get_all()
#         emp = Employee.get_all()
#         ser = self.get_serializer_class()
#         old_data = ser(instance=old, many=True).data
#         vlt_data = ser(instance=vlt, many=True).data
#         emp_data = ser(instance=emp, many=True).data
#         return Response(data={
#             "old_people": old_data,
#             "volunteer": vlt_data,
#             "employee": emp_data
#         }, status=status.HTTP_200_OK)


