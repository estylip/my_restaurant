from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.models import User
from order.models import Cart


def login_user(request):
    if request.user.is_authenticated:
        new_cart=Cart(user_id=request.user.id)   
        new_cart.save()
        return redirect('menu')
    if request.method == "POST":
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                            )
        if user is not None:
            login(request,user)
            new_cart=Cart(user_id=request.user.id)   
            new_cart.save()
            return redirect('menu')
        else:
            return HttpResponse('login failed')
    return render(request,'login.html')


def signup(request):
    if request.method=='POST':
        is_staff=request.POST.get('is_staff')=='on'
        new_user=User(
           username=request.POST['username'],
           password=make_password(request.POST['password']),
           first_name=request.POST['fname'],
           last_name=request.POST['lname'],
           is_staff=is_staff,
           email=request.POST['email']
        )
        new_user.save()
        if new_user.is_staff==True:
            return redirect('manager_login')
        else:
            return redirect('login')
    return render(request,'signup.html')

def manager_login(request):
      if request.method == "POST":
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('../../menu/all_categories')
    
      return render(request,'manager login.html')

@login_required(login_url='signup')
def logout_user(request):
    logout(request)
    return redirect('logo')
    
@login_required(login_url='signup')
def change_details(request, id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.is_staff=user.is_staff
        user.save()
        return redirect('menu')
    return  render(request,'change_details.html',{"user":user})
