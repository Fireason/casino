from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=1000)

    def __str__(self):
        return f"{self.user.username} ({self.balance})"


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city} ({self.latitude}, {self.longitude})"

class Bet(models.Model):
    BET_TYPES = [
        ("temp_gt", "Temperature >"),
        ("rain", "Rain"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None, blank=True, null=True)

    bet_type = models.CharField(max_length=20, choices=BET_TYPES)
    value = models.FloatField(null=True, blank=True)

    amount = models.FloatField()
    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=[
            ("pending", "Pending"),
            ("won", "Won"),
            ("lost", "Lost"),
        ],
        default="pending"
    )

    def __str__(self):
        return f"{self.user} - {self.bet_type}"


class WeatherResult(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None, blank=True, null=True)
    date = models.DateField()

    temperature = models.FloatField()
    rain = models.BooleanField()

    def __str__(self):
        return f"{self.location} {self.date}"