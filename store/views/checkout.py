
from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.orders import Order



#Create your Views here:

class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address,phone, customer_id,cart,products)

        for product in products:
            # print(cart.get(str(product.id)))
            order = Order(
                          customer_id = customer_id,
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          quantity = cart.get(str(product.id)))

            print(order.place_order())
        request.session['cart'] = {}


        return redirect('cart')



