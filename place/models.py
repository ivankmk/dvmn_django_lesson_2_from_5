from django.db import models


class Place(models.Model):
    address = models.CharField('адрес', max_length=250, unique=True)
    latitude = models.FloatField('широта', null=True)
    longitude = models.FloatField('долгота', null=True)
