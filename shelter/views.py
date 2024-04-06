from typing import Any
from django.shortcuts import render
from .models import Dog
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from pytils.translit import slugify

from django.http import HttpResponseRedirect


def dog(request, pk):
    dog = Dog.objects.get(pk=pk)
    context = {
        'dog': dog,
        'title': f"Собака {dog.name}"

    }
    return render(request, 'shelter/dog.html', context)


def home(request):
    dogs = Dog.objects.all()
    context = {
        'dogs': dogs,
        'title': "Питомник для собак"

    }
    return render(request, 'shelter/home.html', context)


class DogListView(ListView):
    model = Dog
    template_name = "shelter/home-cls.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Питомник для собак"

        return context


class DogCreateView(CreateView):
    model = Dog
    fields = ["name", "breed", "birth_date"]
    success_url = reverse_lazy("shelter:home-cls")
    
    def form_valid(self, form):
        dog = form.save()
        dog.slug = slugify(f"{dog.name} {dog.breed.name}")
        dog.save()
        return super().form_valid(dog)
    
    def get_success_url(self) -> str:
        return super().get_success_url()

  
class DogDetailView(DetailView):
    model = Dog
    template_name = "shelter/dog.html"
    