from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from .models import Profile ,BlogPost
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm

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


@login_required(login_url='/login')
def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            messages.success(request,"Blog post added successfully")
            return redirect("/my_post")
    else:
        form = BlogPostForm()
    return render(request,"add_blogs.html",{"form":form})

@login_required(login_url='/login')
def my_post(request):
    user = request.user
    mypost = BlogPost.objects.filter(author=user)
    data = {'mypost':mypost}
    return render(request,"mypost.html",context=data)





