from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api/users/', include("accounts_api.urls", namespace='users-api')),
    url(r'^api/', include("messaging_api.urls", namespace='msg-api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
