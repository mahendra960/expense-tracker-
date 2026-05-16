from encodings.palmos import decoding_table

from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import User, Expense

def home(request):
    return redirect('/expense/register/')


def Register(request):
    return render(request, 'expense/Register.html')

def Registration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        age = request.POST.get("age")
        location = request.POST.get("location")
        User.objects.create_user(username=username, password=password, email=email, age=age, location=location)
        return render(request, 'expense/Login.html')
    else:
        return render(request, 'expense/register.html')

def Login(request):
    return render(request, 'expense/Login.html')

def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            print("user not found")
            return render(request, 'expense/Login.html')
        login(request, user)
        return render(request, 'expense/expenseform.html',{'user':request.user})
    return render(request, 'expense/Login.html')

def Add_details(request):
   if request.method == 'POST':
       user = get_user_model()
       category = request.POST.get("category")
       amount = request.POST.get("amount")
       date = request.POST.get("date")
       user_details = user.objects.filter(username= request.user.username).first()
       user_details_id = user_details.id
       if not user_details_id:
           return render(request, 'expense/Register.html')
       Expense.objects.create(category=category, amount=amount,date=date,user_id=user_details_id)
       expenses = Expense.objects.filter(user_id=user_details_id)
       print(expenses)

       return render(request, 'expense/Result.html',{'expenses':expenses})
   return render(request, 'expense/expenseform.html')





def Result_page(request):
    User = get_user_model()
    expenses = Expense.objects.filter(user_id=User.objects.get(username= request.user.username))
    return render(request, 'expense/Result.html',{'expenses':expenses})

def Results(request):
    User = get_user_model()
    month = request.POST.get("month")
    category = request.POST.get("category")
    user_expenses = Expense.objects.filter(user_id=User.objects.get(username=request.user.username))
    if month != '' and category == 'x':
       expenses = user_expenses.objects.filter(date__month=month)
       return render(request,'expense/ResultPage.html',{'expenses':expenses})
    elif category != '' and month == '':
        expenses = user_expenses.filter(category=category.strip())
        return render(request,'expense/ResultPage.html',{'expenses':expenses})
    else:
        return render(request, 'expense/ResultPage.html',{'expenses':user_expenses})