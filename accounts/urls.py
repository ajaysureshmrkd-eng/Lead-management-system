from django.urls import path

from accounts.views import AdminRegisterView
from accounts.views import UserRegisterView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("admin/",AdminRegisterView.as_view()),

    path("user/",UserRegisterView.as_view()),

    path("user/token/",TokenObtainPairView.as_view()),
    path("user/token/refresh/",TokenRefreshView.as_view()),


]