from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowMain.as_view(), name='shop-home'),
    path('product/<int:pk>/', views.DetailsShowMain.as_view(), name='product-detail'),
    path('product/add/', views.CreateShowMain.as_view(), name='product-add'),
    path('product/<int:pk>/update/', views.UpdateShowMain.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.DeleteProductView.as_view(), name='product-delete'),
    path('order/', views.order, name='shop-order'),
]
