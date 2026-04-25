from django.urls import path
from . import views

urlpatterns = [
    path('', views.bet_page, name='bet_page'),
]