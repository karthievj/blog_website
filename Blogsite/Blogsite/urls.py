"""
URL configuration for Blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.all_posts,name="home"),
    
    #User 
    path('register/',views.register,name="register"),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('reset_password/',views.reset_password,name="reset_password"),
    path('viewprofile/',views.viewprofile,name="viewprofile"),

    #BlogPost
    path('add_blogs/',views.add_blogs,name="add_blogs"),
    path('my_post/',views.my_post,name="my_post"),
    path('search/',views.search,name="search"),
    path('posts/<str:slug>/',views.posts,name="posts"),
    path('comments/<str:slug>',views.blog_comments,name="comments")
]
