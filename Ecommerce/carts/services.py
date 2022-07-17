

import math
from carts.models import CartItems


class CartServices(object):
    def get_total_price(cart_item):
        total_price=0
        for items in cart_item:
            if(items.product.product_name == "pen"):
                item_quantity  = items.quantity
                total_price += item_quantity*items.product.price - math.floor(item_quantity/3) * 15 
            elif (items.product.product_name == "eraser"):
                item_quantity  = items.quantity
                total_price += item_quantity * items.product.price - math.floor(item_quantity/2) * 5
            else:
                total_price += items.price
        return total_price