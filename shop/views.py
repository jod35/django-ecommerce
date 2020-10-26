from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Product

# Create your views here.

def product_list(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={
        'products':products,
        'categories':categories
    }
    return render(request,'shop/product/list.html',context)