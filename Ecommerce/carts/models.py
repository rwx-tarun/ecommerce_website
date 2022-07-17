from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from products.models import *
from django.db.models.signals import pre_save,post_save
from products.models import *
from django.db import models

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)+" "+str(self.total_price)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.user.username)+" "+str(self.product.product_name)


# @receiver(pre_save, sender=CartItems)
# def my_handler(sender, **kwargs):
#     cart_items = kwargs['instance']
#     price_of_product = Product.objects.get(id = cart_items.product.id)
#     cart_items.price = (int)(cart_items.quantity) * price_of_product.price
#     total_cart_items = CartItems.objects.filter(user = cart_items.user)
#     cart_items.total_items = len(total_cart_items)
#     cart = Cart.objects.get(id = cart_items.cart.id)
#     cart.total_price = cart_items.price
#     cart.save()