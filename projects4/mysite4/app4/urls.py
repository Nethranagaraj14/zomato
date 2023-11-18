from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/',views.hotel ,name='hotel'),
    path('login/',views.login_page ,name='login'),
    path('register/',views.register ,name='register'),
    path('food/',views.food ,name='food'),
    path('restaurant/',views.restaurant, name='restaurant'),
    # path('food2/',views.food2 ,name='food2'),
    path('logout/',views.logoutUser, name='logout' ),   
    path('admin_view/', views.admin_view, name='admin_view'),
    path('pay/',views.pay, name='pay'),
    path('food/pay/',views.pay, name='pay'),
    path('seller/',views.seller_view, name='seller'),
     path('addpro/',views.addpro, name='addpro'),
    path('home/', views.home, name='home'),
    
]