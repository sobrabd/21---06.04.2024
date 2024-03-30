from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=200, verbose_name="имя")
    breed = models.ForeignKey("Breed", null=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="dogs", null=True, blank=True)
    birth_date = models.DateField()
    last_update_date = models.DateField(auto_now=True, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ['breed', 'name', ]


class Breed(models.Model):
    name = models.CharField(max_length=200, verbose_name="имя")
    description = models.TextField()