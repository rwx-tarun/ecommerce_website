from itertools import product
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    product_details = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.product_name