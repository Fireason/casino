
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('bets/', include('bets.urls')),

    path('', include('bets.urls')),   # или в корень
]