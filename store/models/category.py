from django.db import models


#create your models here:
class Category(models.Model):
    name = models.CharField(max_length=50)

    # this will give you the all category objects:
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    #with the help of this function we can see the name of this Category in Admin:
    def __str__(self):
        return self.name

