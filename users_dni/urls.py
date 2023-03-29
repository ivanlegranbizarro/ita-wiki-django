from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

app_name = 'users'

urlpatterns = [
    path('register', views.RegisterUserView.as_view(), name='register'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('admin', views.AdminUserView.as_view(), name='admin'),
]
