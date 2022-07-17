import math
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from carts.services import CartServices
from .models import *
from .serializers import *


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        cart = Cart.objects.filter(user = user).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializer(queryset,many=True)
        return Response(serializer.data)


    def post(self,request):
        data = request.data
        user = request.user

        cart,_ = Cart.objects.get_or_create(user = user)
        product = Product.objects.get(id = data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        cart_items = CartItems(cart = cart,user = user,product = product,price =price,quantity=quantity)
        cart_items.save()
        
        cart_items = CartItems.objects.filter(user = user , cart = cart.id)
        total_price=CartServices.get_total_price(cart_item=cart_items)
        cart.total_price = total_price
        cart.save()

        return Response({"success":"item added to cart"})


    def put(self,request):
        data = request.data
        user = request.user
        cart_item = CartItems.objects.get(id = data.get('id'))    
        quantity = data.get('quantity')
        cart_item.quantity +=quantity
        cart_item.save()
        cart,_ = Cart.objects.get_or_create(user = user)
        
        cart_items = CartItems.objects.filter(user = user , cart = cart.id)
        total_price = CartServices.get_total_price(cart_item=cart_items)
        cart.total_price = total_price
        cart.save()
        return Response({"success":"items updated"})
    
    
    def delete(self,request):
        user = request.user
        data = request.data

        cart_item = CartItems.objects.get(id = data.get('id'))
        cart_item.delete()
        
        cart = Cart.objects.filter(user = user).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializer(queryset,many=True)
        return Response(serializer.data)
