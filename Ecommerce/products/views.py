from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product

def details(request, slug):
    context = {'products' : Product.objects.all().filter(slug=slug)}
    return render(request, 'products/details.html', context)
