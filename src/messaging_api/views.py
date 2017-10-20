from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Max
import time
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
)
from .pagination import MsgPageNumberPagination
from django.db.models import Q
from django.contrib.auth import get_user_model
from messaging_api.models import Message
from .serializers import (
    MsgCreateSerializer,
    MsgListSerializer,
    MessageDetailSerializer,
    ConversationCreateSerializer,
    ConversationListSerializer,
    ConversationDetailSerializer,
    ConversationUpdateSerializer
)
from drf_extra_fields.fields import Base64ImageField

User = get_user_model()

class MsgCreateAPIView(CreateAPIView):
    serializer_class = MsgCreateSerializer
    def post(self, request, *args, **kwargs):
        request.data['msg_sender'] = User.objects.get(username=request.data['msg_sender']).id
        request.data['msg_receiver'] = User.objects.get(username=request.data['msg_receiver']).id
        return self.create(request, *args, **kwargs)

class MsgListAPIView(ListAPIView):
    serializer_class = MsgListSerializer
    pagination_class = MsgPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("conversation_id")
        queryset_list = Message.objects.filter(conversation_id=query).order_by('-timestamp')
        return queryset_list

class MsgArchiveAPIView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer
    def put(self, request, *args, **kwargs):
        print(kwargs['pk'])
        return self.update(request, *args, **kwargs)

class MsgDeleteAPIView(DestroyAPIView):
    queryset = Message.objects.all()
    def delete(self, request, *args, **kwargs):
        print(kwargs['pk'])
        return self.destroy(request, *args, **kwargs)

class ConversationCreateAPIView(CreateAPIView):
    serializer_class = ConversationCreateSerializer
    def post(self, request, *args, **kwargs):
        request.data['conversation_id'] = int(round(time.time() * 1000))
        request.data['msg_sender'] = User.objects.get(username=request.data['msg_sender']).id
        request.data['msg_receiver'] = User.objects.get(username=request.data['msg_receiver']).id
        return self.create(request, *args, **kwargs)

class ConversationListAPIView(ListAPIView):
    serializer_class = ConversationListSerializer
    pagination_class = MsgPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("username")
        archived_value = self.request.GET.get('archived').title()
        actions_id = Message.objects.filter(
                Q(msg_sender__username=query) | Q(msg_receiver__username=query) , archived=archived_value
            ).values('conversation_id').annotate(action_id=Max('id')).order_by('-action_id').values_list('action_id', flat=True)
        queryset_list = Message.objects.filter(
                id__in=actions_id
            ).order_by('-timestamp')
        return queryset_list

class ConversationArchivedAPIView(UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = ConversationUpdateSerializer
    lookup_field = 'conversation_id'
    def put(self, request, *args, **kwargs):
        archived_value = request.data['archived']
        instance = Message.objects.filter(conversation_id=kwargs['conversation_id']).update(archived=archived_value)
        return JsonResponse({'success': 'successfully archived message'})

class ConversationDeleteAPIView(DestroyAPIView):
    serializer_class = ConversationListSerializer
    lookup_field = 'conversation_id'
    def delete(self, request, *args, **kwargs):
        instance = Message.objects.filter(conversation_id=kwargs['conversation_id']).delete()
        return JsonResponse({'success': 'successfully deleted message'})
