from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    product_objects = Products.objects.all()
    # Get item list and search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__contains=item_name)
    # pagination code for products
    paginator = Paginator(product_objects,2) # products and number of products in single page
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'shop/index.html',{'product_objects': product_objects})

def detail(request,id):
    product_objects = Products.objects.get(id = id)
    return render(request, 'shop/details.html',{'product_objects': product_objects})