from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.customer import Customer

class Login(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        # read value jo login m user n input kri h
        postData = request.POST
        email = postData.get('email')
        password = postData.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            #login yha ho gya
            if flag:
                #sesion ko save krenge yha
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                #save krne k baad use redirect kr dege
                return redirect('homepage')
            else:
                error_msg = 'Email or password invalid'


        else:
            error_msg = 'Email or password invalid'
        print(customer)
        print(email, password)
        return render(request, 'login.html', {'error': error_msg})


def logout(request):
    request.session.clear()
    return redirect('login')
