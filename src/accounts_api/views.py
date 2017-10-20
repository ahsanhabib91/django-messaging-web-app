from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.views import APIView

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)

from rest_framework.permissions import (
    AllowAny,
)

User = get_user_model()

from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    def get_queryset(self, *args, **kwargs):
        username = self.request.GET.get("username")
        queryset_list = User.objects.filter(~Q(username=username))
        return queryset_list

