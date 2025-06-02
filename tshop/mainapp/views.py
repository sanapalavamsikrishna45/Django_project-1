from django.shortcuts import render
from.models import Product
# Create your views here.


def homeView(request):
    prods = Product.objects.all() #Select * FROMmainapp_products;
    context ={
        'Products' : prods
    }
    template ='home.html'
    return render(request,template,context)  # this renders the response according to the response by using context