from django.db import models

# Create your models here.
class Prods(models.Model):
    ref = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    store = models.CharField(max_length=255)
    amount = models.IntegerField()
    
    def __str__(self):
        txt = "{0} (zipcode {1})"
        return txt.format(self.ref, self.zipcode)

class CoordsProds(models.Model):
    ref_prods = models.ForeignKey(Prods, on_delete=models.CASCADE,verbose_name="Ref Prods")
    lat = models.CharField(max_length=20)
    long = models.CharField(max_length=20)