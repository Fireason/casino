import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "casino_royale.settings")
django.setup()


from bets.models import Bet, City, Location, Profile
from django.contrib.auth.models import User
from bets.services import get_weather


def run():
    print("=== PLAYGROUND START ===")

    user = User.objects.first()

    city, _ = City.objects.get_or_create(name="Amsterdam")

    location = Location.objects.create(
        latitude=52.37,
        longitude=4.89,
        city=city
    )

    bet = Bet.objects.create(
        user=user,
        location=location,
        bet_type="temp_gt",
        value=20,
        amount=100,
        date="2026-04-25"
    )

    print("Created bet:", bet)

    print("=== DONE ===")


if __name__ == "__main__":
    run()