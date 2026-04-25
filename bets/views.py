from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from .services import get_weather

def bet_page(request):

    return render(request, "bets/bet_page.html")

@api_view(['GET'])
def test_weather(request):
    weather = get_weather(52.37, 4.89)
    return JsonResponse(weather)