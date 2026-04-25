from django.shortcuts import render

def bet_page(request):
    return render(request, "bets/bet_page.html")