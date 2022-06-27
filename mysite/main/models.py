from django.db import models


class Shoes(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='img', null=True, blank=True)
    price = models.FloatField(max_length=10)

# Create your models here.
