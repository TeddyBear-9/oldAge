from django.urls import path,re_path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register("oldperson", views.OldPersonModelView, "oldperson")

urlpatterns = [
    # path('', views.index, name='index'),
    # path(r'login/', views.LoginView.as_view(), name='login'),
    path(r'test/', views.TestView.as_view(), name='test'),
    re_path(r'^login/$', TokenObtainPairView.as_view()),
    re_path(r'^refresh/$', TokenRefreshView.as_view()),    # 需要添加的内容
] + router.urls