from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    Serializer,
    FileField,
)
import time
from drf_extra_fields.fields import Base64ImageField
from accounts_api.serializers import UserDetailSerializer

from messaging_api.models import Message
from django.contrib.auth import get_user_model
User = get_user_model()

class MsgCreateSerializer(ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta(object):
        model = Message
        fields = [
            'msg_sender',
            'msg_receiver',
            'message',
            'image',
            'conversation_id',
            'conversation_subject'
        ]

msg_delete_url = HyperlinkedIdentityField(
        view_name='msg-api:msg-delete',
        lookup_field='pk'
    )

msg_archive_url = HyperlinkedIdentityField(
        view_name='msg-api:msg-archived',
        lookup_field='pk'
    )

class MsgListSerializer(ModelSerializer):
    archive_url = msg_archive_url
    delete_url = msg_delete_url
    timestamp = SerializerMethodField()
    msg_sender = UserDetailSerializer(read_only=True)
    msg_receiver = UserDetailSerializer(read_only=True)
    class Meta(object):
        model = Message
        fields = [
            'msg_sender',
            'msg_receiver',
            'message',
            'publish',
            'image',
            'conversation_id',
            'conversation_subject',
            'timestamp',
            'archived',
            'archive_url',
            'delete_url',
        ]
    def get_timestamp(self, object):
        return object.timestamp.strftime("%A %B %d, %Y   %I:%M%p %Z")

class MessageDetailSerializer(ModelSerializer):
    class Meta(object):
        model = Message
        fields = [
            'id',
            'archived',
            'publish',
            'timestamp',
        ]
        
class ConversationCreateSerializer(ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta(object):
        model = Message
        fields = [
            'msg_sender',
            'msg_receiver',
            'message',
            'image',
            'conversation_id',
            'conversation_subject'
        ]
    def create(self, validated_data):
        return Message.objects.create(**validated_data)
    
conv_archived_url = HyperlinkedIdentityField(
        view_name='msg-api:conv-archived',
        lookup_field='conversation_id'
    )
conv_delete_url = HyperlinkedIdentityField(
        view_name='msg-api:conv-delete',
        lookup_field='conversation_id'
    )
class ConversationListSerializer(ModelSerializer):
    archive_url = conv_archived_url
    delete_url = conv_delete_url
    timestamp = SerializerMethodField()
    msg_sender = UserDetailSerializer(read_only=True)
    msg_receiver = UserDetailSerializer(read_only=True)
    class Meta(object):
        model = Message
        fields = [
            'id',
            'msg_sender',
            'msg_receiver',
            'message',
            'image',
            'conversation_id',
            'conversation_subject',
            'publish',
            'timestamp',
            'archive_url',
            'delete_url'
        ]
    def get_timestamp(self, object):
        return object.timestamp.strftime("%A %B %d, %Y   %I:%M%p %Z")

class ConversationDetailSerializer(ModelSerializer):
    class Meta(object):
        model = Message
        fields = [
            'id',
            'archived',
            'publish',
            'timestamp',
        ]

class ConversationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'archived',
            'publish',
            'timestamp',
        ]
