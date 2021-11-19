
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Category, Product
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from .models import *
def Home(request):
    return render(request, 'index.html')

def Cart(request):
    return render(request, 'cart.html')

def Checkout(request):
    return render(request, 'checkout.html')

def Product_Details(request):
    return render(request, 'product-details.html')

def Shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'shop.html', context)


# Create your views here.
