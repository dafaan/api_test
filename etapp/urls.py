from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.more, name='more'),
    path('contact/', views.contact, name='contact'),
]