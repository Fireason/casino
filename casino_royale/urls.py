from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include

schema_view = get_schema_view(
    openapi.Info(
        title="Weather Casino API",
        default_version='v1',
        description="API для ставок на погоду",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('bets/', include('bets.urls')),

    path('', include('bets.urls')),   # или в корень
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0)),
]