from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import customer
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

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    fname = request.POST.get('fname')
    e_mail = request.POST.get('e_mail')
    phone = request.POST.get('phone')
    passw = request.POST.get('passw')

    Customer = customer(name = fname,
                        e_mail = e_mail,
                        phone = phone,
                        password = passw)
    Customer.save()
    return redirect('homepage')