from django.contrib import admin
from .models import Profile, City, Bet, WeatherResult


admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Bet)
admin.site.register(WeatherResult)