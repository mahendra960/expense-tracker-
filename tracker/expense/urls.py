from django.shortcuts import redirect
from django.urls import path

from . import views


app_name = 'expense'
urlpatterns = [
   path('register/', views.Register, name='register'),
    path('registration/', views.Registration, name='registration'),
    path('login/', views.Login, name='login'),
    path('login_page/', views.Login_page, name='Login_page'),
    path('result/', views.Result_page, name='Result'),
    path('form/', views.Add_details, name='expense_form'),
    path('results/', views.Results, name='results'),

path('', views.home, name='home'),
]