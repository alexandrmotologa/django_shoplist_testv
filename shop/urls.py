from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('order/', views.order, name='shop-order'),
]
