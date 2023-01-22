from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('staff/', views.staff, name='staff'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('profile/', views.profile, name='profile'),
    ]