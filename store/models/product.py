from django.db import models
from .category import Category
class Product(models.Model):
    Name = models.CharField(max_length=53)
    Price = models.IntegerField(default=0)
    Category = models.ForeignKey(Category, on_delete= models.CASCADE , default = 1)
    Description = models.CharField(max_length=200, default='')
    Image = models.ImageField(upload_to='uploads/productsimage/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if(category_id):
            return Product.objects.filter(Category_id=category_id)
        else:
            return Product.objects.all()

