from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product


def complete(request):
    searched_name_product = request.GET.get("searched_name")
    product = Product.objects.find_products(searched_name_product)
    product = [product.product_name for product in products]
    return JsonResponse(product, safe=False)
