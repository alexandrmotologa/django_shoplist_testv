from django.shortcuts import render
from .models import Product


def home(request):
    data = {
        'product': Product.objects.all(),
        'title': 'Home Page'
    }
    return render(request, 'shop/home.html', data)

def order(request):
    return render(request, 'shop/order.html')
