from django.views import View
from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password



class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')

    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(first_name, last_name, phone, email, password)


        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_msg = self.validateCustomer(customer)

        # Saving

        if error_msg:
            value = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email
            }
            data = {
                'values': value,
                'error': error_msg
            }
            return render(request, 'signup.html', data)
        else:

            # hashing the password
            customer.password = make_password(customer.password)
            customer.register()

            return redirect('homepage')

    # Validation:
    # Now we need to save this value so hm ise customer m ek method bnake save krenge:
    def validateCustomer(self, customer):

        error_msg = None
        # first_name validation:
        if not customer.first_name:
            error_msg = 'First name required'
        elif len(customer.first_name) < 4:
            error_msg = 'First name must be 4 char long or more'

        # last_name validation:
        if not customer.last_name:
            error_msg = 'Last name required'
        elif len(customer.last_name) < 4:
            error_msg = 'last name must be 4 char or more'

        # phone number validation:
        if not customer.phone:
            error_msg = 'Phone number required'
        elif len(customer.phone) < 10:
            error_msg = 'phone number must be 10 char or more'

        # password validation:
        if not customer.password:
            error_msg = 'password required'
        elif len(customer.password) < 5:
            error_msg = 'password must be 5 char or more'

        # isExists = customer.isExists()
        # if isExists:
        #     error_msg = 'this email is already registered'
        # ------------or----------
        elif customer.isExists():
            error_msg = 'this email is already registered'

        return error_msg