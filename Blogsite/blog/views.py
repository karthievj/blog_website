from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from .models import Profile

# Create your views here.


def home(request):
    return render(request,"home.html")


def register(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = f"{fname}{lname}"
        dob = request.POST['dob']
        age = request.POST['age']
        mnumber = request.POST['mnumber']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
    
        if password != password1:
            messages.error(request,"Passwords does not match")
            return redirect("/register")
        user = User.objects.create_user(username,
                                        email,
                                        password1,
                                       )
        user.first_name = fname
        user.last_name = lname
        user.save()
        profile = Profile.objects.create(user=user,
                                        dob=dob,
                                        age=age,
                                        mnumber=mnumber)
        messages.success(request,f"User registered successfully...Use username as {username} to login to the website")
        return render(request,"login.html")
    return render(request,"register.html")

def login_user(request):
    if request.method=="POST":
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=uname,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in...")
            return redirect("/")
        else:
            messages.error(request,"Invalid login details ")
        return render(request,"home.html")
    return render(request,"login.html")

def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("home")

def reset_password(request):
    return HttpResponse("reset your password")



