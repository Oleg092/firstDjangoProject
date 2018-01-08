from django.db import models


class Departament(models.Model):
    website = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class People(models.Model):
    name = models.CharField(max_length=20)
    surName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    birdDate = models.DateField()
    email = models.EmailField()
    photo = models.CharField(max_length=50)
    departament = models.ForeignKey(
        Departament,
        on_delete=models.CASCADE,
    )
