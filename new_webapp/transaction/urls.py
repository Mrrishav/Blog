from django.contrib import admin
from django.urls import path
from transaction import views

urlpatterns = [
    path('deposit',views.deposit, name="deposit"),
    path('amtfer',views.amtfer, name="amtfer"),
]