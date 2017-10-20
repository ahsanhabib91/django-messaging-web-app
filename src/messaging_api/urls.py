from django.conf.urls import url
from django.contrib import admin

from .views import (
    MsgCreateAPIView,
    MsgListAPIView,
    MsgArchiveAPIView,
    MsgDeleteAPIView,

    ConversationCreateAPIView,
    ConversationListAPIView,
    ConversationDeleteAPIView,
    ConversationArchivedAPIView,

)

urlpatterns = [
    url(r'^message/create$', MsgCreateAPIView.as_view(), name='msg-create'),
    # url(r'^message/create/(?P<msg_sender>[\w-]+)/(?P<msg_receiver>[\w-]+)/(?P<message>[\w-]+)/(?P<conversation_id>[\w-]+)/(?P<conversation_subject>[\w-]+)/$', MsgCreateAPIView.as_view(), name='msg-create'),
    url(r'^messages/$', MsgListAPIView.as_view(), name='msg-list'),
    url(r'^message/archived/(?P<pk>\d+)/$', MsgArchiveAPIView.as_view(), name='msg-archived'),
    url(r'^message/delete/(?P<pk>\d+)/$', MsgDeleteAPIView.as_view(), name='msg-delete'),
    
    
    url(r'^conversation/create$', ConversationCreateAPIView.as_view(), name='conv-create'),
    url(r'^conversations/$', ConversationListAPIView.as_view(), name='conv-list'),
    url(r'^conversation/archived/(?P<conversation_id>[\w-]+)/$', ConversationArchivedAPIView.as_view(), name='conv-archived'),
    url(r'^conversation/delete/(?P<conversation_id>[\w-]+)/$', ConversationDeleteAPIView.as_view(), name='conv-delete'),
]