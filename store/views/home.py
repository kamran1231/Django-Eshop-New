from django.shortcuts import render, HttpResponse,redirect
from store.models.category import Category
from store.models.product import Product
from django.views import View



# Create your views here.
class Index(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        categories = Category.get_all_categories()
        # this hold the touch category id which we click during the categories
        # hm jb click krege category m to y uski id store kr lega:
        categoryId = request.GET.get('category')  # y 'category' index.html s aayegi jo hmne query string m ki h
        if categoryId:
            products = Product.get_all_products_by_categoryId(categoryId)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        print(request.session.get('email'))

        return render(request, 'index.html', data)

    def post(self,request):

        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1




        # now we will update session:
        request.session['cart'] = cart
        print(cart)
        return redirect('homepage')








# def index(request):
#     products = None
#     categories = Category.get_all_categories()
#     # this hold the touch category id which we click during the categories
#     # hm jb click krege category m to y uski id store kr lega:
#     categoryId = request.GET.get('category')  # y 'category' index.html s aayegi jo hmne query string m ki h
#     if categoryId:
#         products = Product.get_all_products_by_categoryId(categoryId)
#     else:
#         products = Product.get_all_products()
#
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print(request.session.get('email'))
#
#     return render(request, 'index.html', data)

# class Signup(View):
#     def get(self,request):
#         return render(request, 'signup.html')
#
#     def post(self,request):
#         postData = request.POST
#         first_name = postData.get('firstname')
#         last_name = postData.get('lastname')
#         phone = postData.get('phone')
#         email = postData.get('email')
#         password = postData.get('password')
#         print(first_name, last_name, phone, email, password)
#
#         # Validation:
#         # Now we need to save this value so hm ise customer m ek method bnake save krenge:
#         customer = Customer(first_name=first_name,
#                             last_name=last_name,
#                             phone=phone,
#                             email=email,
#                             password=password)
#         error_msg = self.validateCustomer(customer)
#
#         # Saving
#
#         if error_msg:
#             value = {
#                 'first_name': first_name,
#                 'last_name': last_name,
#                 'phone': phone,
#                 'email': email
#             }
#             data = {
#                 'values': value,
#                 'error': error_msg
#             }
#             return render(request, 'signup.html', data)
#         else:
#
#             # hashing the password
#             customer.password = make_password(customer.password)
#             customer.register()
#
#             return redirect('homepage')
#
#     def validateCustomer(self, customer):
#
#         error_msg = None
#         # first_name validation:
#         if not customer.first_name:
#             error_msg = 'First name required'
#         elif len(customer.first_name) < 4:
#             error_msg = 'First name must be 4 char long or more'
#
#         # last_name validation:
#         if not customer.last_name:
#             error_msg = 'Last name required'
#         elif len(customer.last_name) < 4:
#             error_msg = 'last name must be 4 char or more'
#
#         # phone number validation:
#         if not customer.phone:
#             error_msg = 'Phone number required'
#         elif len(customer.phone) < 10:
#             error_msg = 'phone number must be 10 char or more'
#
#         # password validation:
#         if not customer.password:
#             error_msg = 'password required'
#         elif len(customer.password) < 5:
#             error_msg = 'password must be 5 char or more'
#
#         # isExists = customer.isExists()
#         # if isExists:
#         #     error_msg = 'this email is already registered'
#         # ------------or----------
#         elif customer.isExists():
#             error_msg = 'this email is already registered'
#
#         return error_msg
#
#
# class Login(View):
#     def get(self,request):
#         return render(request, 'login.html')
#
#     def post(self,request):
#         # read value jo login m user n input kri h
#         postData = request.POST
#         email = postData.get('email')
#         password = postData.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_msg = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_msg = 'Email or password invalid'
#
#
#         else:
#             error_msg = 'Email or password invalid'
#         print(customer)
#         print(email, password)
#         return render(request, 'login.html', {'error': error_msg})





#----------------function------------------

# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return registerUser(request)

# def validateCustomer(customer):
#
#     error_msg = None
#     # first_name validation:
#     if not customer.first_name:
#         error_msg = 'First name required'
#     elif len(customer.first_name) < 4:
#         error_msg = 'First name must be 4 char long or more'
#
#     # last_name validation:
#     if not customer.last_name:
#         error_msg = 'Last name required'
#     elif len(customer.last_name) < 4:
#         error_msg = 'last name must be 4 char or more'
#
#     # phone number validation:
#     if not customer.phone:
#         error_msg = 'Phone number required'
#     elif len(customer.phone) < 10:
#         error_msg = 'phone number must be 10 char or more'
#
#     # password validation:
#     if not customer.password:
#         error_msg = 'password required'
#     elif len(customer.password) < 5:
#         error_msg = 'password must be 5 char or more'
#
#     # isExists = customer.isExists()
#     # if isExists:
#     #     error_msg = 'this email is already registered'
#     # ------------or----------
#     elif customer.isExists():
#         error_msg = 'this email is already registered'
#
#     return error_msg


# def registerUser(request):
#     postData = request.POST
#     first_name = postData.get('firstname')
#     last_name = postData.get('lastname')
#     phone = postData.get('phone')
#     email = postData.get('email')
#     password = postData.get('password')
#     print(first_name, last_name, phone, email, password)
#
#     # Validation:
#     # Now we need to save this value so hm ise customer m ek method bnake save krenge:
#     customer = Customer(first_name=first_name,
#                         last_name=last_name,
#                         phone=phone,
#                         email=email,
#                         password=password)
#     error_msg = validateCustomer(customer)
#
#     # Saving
#
#     if error_msg:
#         value = {
#             'first_name': first_name,
#             'last_name': last_name,
#             'phone': phone,
#             'email': email
#         }
#         data = {
#             'values': value,
#             'error': error_msg
#         }
#         return render(request, 'signup.html', data)
#     else:
#
#         # hashing the password
#         customer.password = make_password(customer.password)
#         customer.register()
#
#         return redirect('homepage')



# def login(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
#     else:
#         #read value jo login m user n input kri h
#         postData = request.POST
#         email = postData.get('email')
#         password = postData.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_msg = None
#         if customer:
#             flag = check_password(password,customer.password)
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_msg = 'Email or password invalid'
#
#
#         else:
#             error_msg = 'Email or password invalid'
#         print(customer)
#         print(email,password)
#         return render(request,'login.html',{'error':error_msg})


#-------------------------Function End----------------------------
