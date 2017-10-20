from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserListAPIView
)

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^$', UserListAPIView.as_view(), name='user-list'),
]