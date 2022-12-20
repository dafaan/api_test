from django.urls import path
from .views import *

urlpatterns = [
    path('', itemCreateView.as_view()),
    path('users/', getuser)
]