from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('generate', views.index),
    path('reset', views.reset),
]