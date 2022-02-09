from django.shortcuts import render

from .models import Product,Brand
# Create your views here.

def index(request):
    brands = len(Brand.objects.all())
    producs = len(Product.objects.all())

    return render(request, 'makeup/index.html',{
        'brands':brands,
        'producs':producs
    })

def product_details(request, makeup_name):
    try:
        product = Product.objects.get(name = makeup_name)
        return render(request, 'makeup/product_details.html',{
            'found':True,
            'pro':product 
        })
    except Exception as ex:
        return render(request, 'makeup/product_details.html',{
            'found':False,
        })

def brand_details(request, brand_name):
    try:
        brands = Brand.objects.get(Name = brand_name)
        return render(request, 'makeup/brand_details.html',{
            'found':True,
            'brand':brands 
        })
    except Exception as ex:
        return render(request, 'makeup/product_details.html',{
            'found':False,
        })
def Products(request):
    products = Product.objects.all()

    return render(request, 'makeup/Products.html',{
        'products':products
    })

def Brands(request):
    brands = Brand.objects.all()
    
    return render(request, 'makeup/Brands.html',{
        'brands':brands
    })