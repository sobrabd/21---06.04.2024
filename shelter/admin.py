from django.contrib import admin
from .models import Dog, Breed


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['name', "breed", "last_update_date", "creation_date"]
    list_filter = ['breed']



@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass