from django.shortcuts import render


def restaurant_orders(request):
    return render(request, 'restaurant.html', {})
