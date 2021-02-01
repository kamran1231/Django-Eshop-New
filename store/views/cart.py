from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product



#Create your Views here:

class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})
