from django.urls import path
from . import views

urlpatterns = [
    path('inquery', views.contact, name='inquery'),
]
