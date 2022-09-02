"""instakilo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from.import views



urlpatterns = [
    path("",views.Login,name="login"),
    path("singup", views.singup, name="singup"),
    path("home", views.home, name="home"),
    path("profile", views.profile, name="profile"),
    path("Logout", views.Logout, name="Logout"),
    path("search", views.search, name="search"),
    path("searchuserprofile/<int:userid>", views.searchuserprofile, name="searchuserprofile"),
    path("follow/<int:id>", views.follow, name="follow"),
    path("post", views.post, name="post"),
    path("like/<int:postid>", views.like, name="like"),
    path("comment/<int:postid>", views.comments, name="comment"),
    path("upload/<int:postid>", views.upload, name="upload"),
    path("likeview/<int:postid>", views.likeview, name="likeview"),
    path("postfullview/<int:postid>", views.postfullview, name="postfullview"),
    path("delete/<int:postid>", views.delete, name="delete"),



]
