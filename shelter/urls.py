from django.urls import path
from .apps import  ShelterConfig

from . import views
app_name = ShelterConfig.name

urlpatterns = [
    path("dog/<int:pk>", views.dog, name="dog"),
    path('', views.home, name="home")
]

