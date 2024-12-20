from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('search/', views.search, name='search'),
]
