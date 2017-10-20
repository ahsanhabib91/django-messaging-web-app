from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

User = get_user_model()

class UserDetailSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]
            
class UserListSerializer(ModelSerializer):
    class Meta(object):
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name'
        ]

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            
        ]
        extra_kwargs = {"password":{ "write_only" : True }}
    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return data
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username = username,
                email = email
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
