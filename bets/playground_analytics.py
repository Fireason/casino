import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "casino_royale.settings")
django.setup()


from bets.models import Bet, City, Location, Profile
import requests
from django.contrib.auth.models import User
from bets.services import get_weather


def run():
    print("=== PLAYGROUND START ===")
    weather = get_weather(52.37, 4.89)
    print("Weather:", weather)

    print("=== DONE ===")


if __name__ == "__main__":
    run()