
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

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
    return render(request, 'shop.html')
# Create your views here.
