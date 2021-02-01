from django.db import models




#Create your models here:
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    
    def register(self):
        self.save()


    #email unique:
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False





