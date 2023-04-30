from django.shortcuts import render, redirect
from .models import Category, Dish
from django.contrib.auth.decorators import login_required


@login_required(login_url='manager_login')
def all_categories(request):
    categories=Category.objects.all()
    return render(request,'category_managment.html',{'category_list':categories})

@login_required(login_url='manager_login')
def add_category(request):
    if request.method=='POST':
        new_category=Category(
           name=request.POST['name'],
           imageUrl=request.POST['imageUrl'] 
        )
        new_category.save()
        return redirect(all_categories)
    return render(request,'add_category.html')

@login_required(login_url='manager_login')
def edit_category(request,id):
    category=Category.objects.get(id=id)
    if request.method=='POST':
        category.name=request.POST['name']
        category.imageUrl=request.POST['imageUrl']
        category.save()
        return redirect(all_categories)
    return render(request,'edit_category.html',{"category":category})

@login_required(login_url='manager_login')
def delete_category(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    return redirect(all_categories)

@login_required(login_url='manager_login')
def all_dishes(request):
    dishes_list=Dish.objects.all()
    return render(request,'dishes_managment.html',{"dishes":dishes_list})

@login_required(login_url='manager_login')
def add_dish(request):
    is_gloten_free=request.POST.get('is_gloten_free')=='on'
    is_vegetarian=request.POST.get('is_vegetarian')=='on'
    if request.method=='POST':
        new_dish=Dish(
            name=request.POST['name'],
            price=request.POST['price'],
            description=request.POST['description'],
            imageUrl=request.POST['imageUrl'],
            is_gloten_free=is_gloten_free,
            is_vegetarian=is_vegetarian,
            category_id=request.POST['categories'],        
        )
        new_dish.save()
        return redirect(all_dishes)
    categories=Category.objects.all()
    return render(request,'add_dish.html',{"categories":categories})

@login_required(login_url='manager_login')
def edit_dish(request,id):
    dish=Dish.objects.get(id=id)
    categories=Category.objects.all()
    is_gloten_free=request.POST.get('is_gloten_free')=='on'
    is_vegetarian=request.POST.get('is_vegetarian')=='on'
    if request.method=='POST':
        dish.name=request.POST['name']
        dish.price=int(request.POST['price'])
        dish.description=request.POST['description']
        dish.imageUrl=request.POST['imageUrl']
        dish.is_gloten_free=is_gloten_free
        dish.is_vegetarian=is_vegetarian
        dish.category.id=request.POST['categories']
        dish.save()
        return redirect(all_dishes) 
    return render(request,'edit_dish.html',{"dish":dish,"categories": categories})

@login_required(login_url='manager_login')
def delete_dish(request,id):
    dish=Dish.objects.get(id=id)
    dish.delete()
    return redirect(all_dishes)

@login_required(login_url='login')   
def show_menu(request):
    dish_list=Dish.objects.all()
    categories=Category.objects.all()
    return render(request,'menu.html',{"categories": categories ,"dish_list":dish_list})

@login_required(login_url='login')
def dish_by_category(request, id):
    dish_list=Dish.objects.all()
    category=Category.objects.get(id=id)
    
    return render(request,'dish_by_category.html',{"dish_list":dish_list,"category":category})