from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from . models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    context={}
    return render(request, 'home.html',context)

@login_required(login_url= 'login')
def hotel(request):
    return render(request, 'hotel.html')


def login_page(request):
    # {% if user.is_authenticated %}

    # # if request.user is_authenticated():
    #     return redirect('index')
    
    # {% else %}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('admin_view')
            else:
                messages.info(request, 'Username Or password is incorrect')
                return render(request, 'login.html')

        return render(request, 'login.html')
    # {% endif %}

def register(request):
    # if request.user is_authenticated():
    #     return redirect('index')
    # else
    #     form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                messages.success(request,'Account was created for ' + user )
                return redirect('login')
        context={'form':form}
        return render(request, 'register.html',context)

@login_required(login_url= 'login')
@allowed_users(allowed_roles=['customer'])
def food(request):
    food_objects = Food.objects.all()
    # food_objects = Food.objects.filter(restaurant=restaurant)

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        food_objects = food_objects.filter(title__icontains=item_name)
    return render(request, 'food.html', {'food_objects':food_objects})

@login_required(login_url= 'login')
@allowed_users(allowed_roles=['customer'])
def restaurant(request):
    # customer = customer.objects.get(id=pk_test)
    restaurant_objects = Restaurant.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        restaurant_objects = restaurant_objects.filter(title__icontains=item_name)
    return render(request,'restaurant.html',{'restaurant_objects':restaurant_objects})

@login_required(login_url= 'login')
def logoutUser(request):
    logout(request)
    return redirect('login')


# def food2(request):
#     food2_objects = Food2.objects.all()

#     item_name = request.GET.get('item_name')
#     if item_name != '' and item_name is not None:
#         food2_objects = food2_objects.filter(title__icontains=item_name)
#     return render(request, 'food2.html',{'food2_objects':food2_objects})


def my_view(request):
    context = {
        'content': 'This is the content below the background image.',
    }
    return render(request, 'index.html', context)

@login_required(login_url= 'login')
def pay(request):
    if request.method == 'POST':
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        username = request.POST.get('username')
        Address = request.POST.get('Address')
        Name_on_card = request.POST.get('Name_on_card')
        Credit_card_number = request.POST.get('Credit_card_number')
        Name_on_card = request.POST.get('Name_on_card')
        Expiration = request.POST.get('Expiration')
        CVV = request.POST.get('CVV')
        pincode = request.POST.get('pincode')
        # quantity = request.POST.get('quantity')
        # title = Food.objects.first()
        
        Pay.objects.create(First_name = First_name,Last_name = Last_name, username = username,Address = Address,Credit_card_number = Credit_card_number,Name_on_card = Name_on_card,Expiration = Expiration,CVV = CVV, pincode = pincode)
        return render(request, "pay.html")
    else:
        return render(request, "pay.html")


@login_required(login_url='login')
def seller_view(request):
    restaurant_objects = Restaurant.objects.all()
    context = {'restaurant_objects':restaurant_objects}
    return render(request, 'seller.html', context)





@login_required(login_url= 'login')
@admin_only
def admin_view(request):
    context = {}
    return render(request, 'admin.html', context)

    
@login_required(login_url= 'login')
def addpro(request):
    context = {}
    return render(request, 'addpro.html', context)