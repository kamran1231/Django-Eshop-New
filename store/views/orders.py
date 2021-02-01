

from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.orders import Order
from store.middleware.auth import auth_middleware



#Create your Views here:

class Orders(View):

    def get(self,request):
        customer_id = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer_id)
        print(orders)
        return render(request,'orders.html',{'orders':orders})









