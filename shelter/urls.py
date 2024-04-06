from django.urls import path
from .apps import ShelterConfig


from . import views
app_name = ShelterConfig.name

urlpatterns = [
    path("dog/<int:pk>", views.dog, name="dog"),
    path('', views.home, name="home"),
    path('cls-home', views.DogListView.as_view(), name="home-cls"),
    path('create_dog', views.DogCreateView.as_view(), name="dog-create"),
    path("dog-slug/<slug:slug>", views.DogDetailView.as_view(), name="dog_slug"),

]

