from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import customer

class AdminProduct(admin.ModelAdmin):
    list_display = ['Name', 'Price', 'Category']

class AdminCategoru(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','e_mail','phone']
# Register your models here.

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategoru)
admin.site.register(customer, AdminCustomer)