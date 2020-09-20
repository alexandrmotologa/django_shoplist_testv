from django.shortcuts import render
from .models import Product
from django.utils import timezone


def home(request):
    now = timezone.now().strftime("%Y-%m-%d %H:%M")
    data = {
        'product': Product.objects.all(),
        'title': 'Home Page',
        'time': now
    }
    return render(request, 'shop/home.html', data)

def order(request):
    now = timezone.now().strftime("%Y-%m-%d %H:%M")
    data = {
        'time': now
    }
    return render(request, 'shop/order.html', data)
