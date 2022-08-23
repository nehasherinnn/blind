from django.urls import path
from .import views
urlpatterns=[
    path('',views.cart,name="cart"),
    path('item',views.item,name="item"),
    path('home',views.home,name="home"),
]