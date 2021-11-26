from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from BPshop.models import *
from .Cart import *
from .Forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    print("ЭТО ПРОДУКТ ID",product_id)
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    print=("ЭТО КОРЗИНА!!!",cart)
    return render(request, 'Cart/cart.html',{'cart': cart})