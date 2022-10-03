from django.db import models

# Create your models here.
class Prods(models.Model):
    ref = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    store = models.CharField(max_length=255)
    amount = models.IntegerField()