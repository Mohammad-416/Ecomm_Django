from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from products.models import Product
from django.contrib import messages

def index(request):
    context = {'products' : Product.objects.all()}
    return render(request, 'home/index.html', context )

def category(request):
    return render(request, 'home/category.html') 

def clients(request):
    return render(request, 'home/clients.html') 

def products(request):
    context = {'products' : Product.objects.all()}
    return render(request, 'home/products.html', context) 

def contact(request):
    return render(request, 'home/contact.html') 