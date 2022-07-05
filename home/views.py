from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt import authentication
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView, \
    GenericAPIView, DestroyAPIView, UpdateAPIView

from .serializers import *


class TestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        return Response('ok')


class OldPersonModelView(ModelViewSet):
    queryset = OldPerson.get_all()
    serializer_class = OldPersonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.remove = 'y'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeModelView(ModelViewSet):
    queryset = Employee.get_all()
    serializer_class = EmpolyeeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.remove = 'y'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VolunteerModelView(ModelViewSet):
    queryset = Volunteer.get_all()
    serializer_class = VolunteerSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.remove = 'y'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
