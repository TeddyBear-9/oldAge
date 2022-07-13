from django.urls import path,re_path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register("oldperson", views.OldPersonModelView, "oldperson")
router.register("employee", views.EmployeeModelView, "employee")
router.register("volunteer", views.VolunteerModelView, "volunteer")
router.register("event", views.EventModelView, "event")
# router.register("face_inf", views.GetFaceView, "face")

urlpatterns = [

    re_path(r'^login/$', TokenObtainPairView.as_view()),
    re_path(r'^refresh/$', TokenRefreshView.as_view()),    # 需要添加的内容
    path('chat/', views.index, name='index'),
] + router.urls