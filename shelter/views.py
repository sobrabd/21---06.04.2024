from django.shortcuts import render
from .models import Dog


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