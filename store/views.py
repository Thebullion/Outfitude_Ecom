from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
# Create your views here.
def index(request):
    product = None
    cat = Category.get_all_cat()
    category_id = request.GET.get('category_id')
    if(category_id):
        product = Product.get_all_products_by_id(category_id)
    else:
        product = Product.get_all_products()


    data={}
    data['product'] = product
    data['cat'] = cat

    return render(request, 'index.html', data)



