from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products=Product.objects.all()
    
    print(products)
    return render(request,"home/index1.html",{
        'prod':products,
    })



def try_clothes_on(request,id):
    products=Product.objects.all()
    p_id=Product.objects.get(pk=id)
    return render(request,"home/tryon.html",{
        'prod':products,
        'id':p_id
    })

