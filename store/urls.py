from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('',views.store, name='store'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('update_item/',views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.loginPage, name="logout"),
    path('', auth_views.LoginView.as_view()),
    path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon/favicon.ico')),
]

