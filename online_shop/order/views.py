from django.shortcuts import render
from user.models import Costumer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from cart.views import generate_unique_cart_code
from cart.models import Cart
from order.models import Order

def finalize_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.is_received = True
        JsonResponse({"message" : "Order is received"}, safe=False)
    except Order.DoesNotExist:
        JsonResponse({"error" : "Order does not exist"}, safe=False)

def view_costumer_orders(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            costumer_id = data['costumer_id']
            costumer_order = Order.objects.filter(costumer__id=costumer_id)
            order_list = []
            for order in costumer_order:
                order_list.append({
                    'order code' : order.code,
                    'costumer' : order.costumer.name,
                    'is reached' : order.is_received,
                    'products' : list(order.products.values('name'))
                })
            return JsonResponse(order_list, safe=False)
        except Order.DoesNotExist:
            return JsonResponse({"error" : "Order does not exist"}, safe=False)
    else:
        return JsonResponse({"error" : "Method not allowed"}, safe=False)

