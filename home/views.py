from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView, \
    GenericAPIView, DestroyAPIView, UpdateAPIView

from .authentication import MyJWTAuthentication
from .models import *
from .serializers import *


class TestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        return Response('ok')


class OldPersonModelView(ModelViewSet):
    queryset = OldPerson.get_all()
    serializer_class = OldPersonSerializer
    # permission_classes = permission
    # authentication_classes = [MyJWTAuthentication, SessionAuthentication, BasicAuthentication]


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

# class LoginView(APIView):

#
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
