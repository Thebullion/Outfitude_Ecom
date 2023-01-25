from django.contrib import admin
from .models.product import Product
from .models.category import Category

class AdminProduct(admin.ModelAdmin):
    list_display = ['Name', 'Price', 'Category']

class AdminCategoru(admin.ModelAdmin):
    list_display = ['name']
# Register your models here.

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategoru)