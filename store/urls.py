
from django.contrib import admin
from django.urls import path
from .views import Index,Signup,Login,logout,Cart,CheckOut,Orders
from .middleware.auth import auth_middleware


urlpatterns = [
    path('',Index.as_view(),name='homepage' ),
    path('signup',Signup.as_view(),name='signup' ),
    path('login',Login.as_view(),name='login' ),
    path('cart',Cart.as_view(),name='cart' ),
    path('logout',logout,name='logout' ),
    path('check-out',CheckOut.as_view(),name='checkout' ),
    path('orders',auth_middleware(Orders.as_view()),name='orders' ),
]
