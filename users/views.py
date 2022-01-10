from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from gram.models import Profile

# Create your views here.
def register(request):
   
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            
            user = authenticate(username=username,password=password)
            Profile.objects.create(user=user)
            login(request,user)
            print(request.POST)
            messages.success(request,f"Congratulations, your account was successfully created under {username}")
            return redirect('home')
         else:
            messages.success(request,f"Sorry, account was not created. Please try again.")
            return redirect('register')


    else:
        form = UserCreationForm()
        return render(request,'auth/register.html',{"form":form})
        

   

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
           
            return redirect('home')
        else:
            messages.success(request,"Login unsuccessful check either your username or your password")
            return render(request,'auth/login.html')

    else: 
        return render(request,'auth/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'You were logged out')
    return redirect('login')