from django.db import models
from store.models.category import Category


#Create your models here:

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')


    @staticmethod
    def get_all_products():
        return Product.objects.all()


    #with the help of this function we will filter category:
    @staticmethod
    def get_all_products_by_categoryId(category_id): #y id aayegi view ki id s jb hm click krte h:
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()


    #cart m kitne product h:
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

