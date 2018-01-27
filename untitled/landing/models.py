from django.db import models


class People(models.Model):
    name = models.CharField(max_length=20)
    surName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
