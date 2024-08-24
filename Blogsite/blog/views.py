from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from .models import Profile ,BlogPost ,Comments
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
            return redirect("/my_post")
        else:
            messages.error(request,"Invalid login details ")
            return redirect("/login_user")
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
    mypost = BlogPost.objects.filter(author=user).order_by('-date_time')
    data = {'mypost':mypost}
    return render(request,"mypost.html",context=data)

def all_posts(request):

    # all_post = BlogPost.objects.all()
    all_post = BlogPost.objects.filter().order_by('-date_time')
    return render(request,"home.html",{'all_post':all_post})

def search(request):
    if request.method == "POST":
       searched = request.POST['searched']
       print(searched,'fkjakljsflk')
       if searched!="":
            search_blogs = BlogPost.objects.filter(title__contains=searched).order_by('-date_time')
            if search_blogs:
                blog_count = len(search_blogs)
                data = {'searched':searched,'search_blogs':search_blogs,'blog_count':blog_count}
                return render(request, "search.html",context=data)
            else:
                messages.success(request,f"No blogs related to {searched}...Search different blogs")
                return redirect('home')
       else:
            messages.success(request,f"Enter any title to search")
            return redirect('home')
    else:
        return render(request,"search.html",{})


def posts(request,slug):
    single_post = BlogPost.objects.filter(slug=slug).order_by('-date_time')
    return render(request,"post.html",context={'single_post':single_post})

def blog_comments(request,slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comments.objects.filter(blog=post)
    data = {'post':post,'comments':comments}
    if request.method=="POST":
        user=request.user
        content=request.POST['content']
        comment = Comments(user=user,content=content,blog=post)
        comment.save()
    return render(request,"blogs_comments.html",context=data)

def viewprofile(request):
    return HttpResponse("view profile")
    



