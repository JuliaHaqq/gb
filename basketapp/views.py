from django.contrib import auth
from django.http import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from basketapp.models import Basket

from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

@login_required
def basket(request):
    baskets_list = Basket.objects.filter(user=request.user)

    context = {
        'basket': baskets_list
    }

    return render(request, 'basketapp/basket.html', context)

@login_required
def add(request, pk):
    product_item = get_object_or_404(Product, pk=pk)

    basket_item = Basket.objects.filter(product = product_item, user=request.user).first()

    if not basket_item:
        basket_item = Basket(product=product_item, user=request.user)

    basket_item.quantity += 1
    basket_item.save() 

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def remove(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        basket_item = Basket.objects.get(pk=pk)

        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
        else:
            basket_item.delete()

        basket_list = Basket.objects.filter(user=request.user)

        context = {
            'baskets': basket_list
        }

        result = render_to_string('', context)
        
        return JsonResponse({'result':result})
