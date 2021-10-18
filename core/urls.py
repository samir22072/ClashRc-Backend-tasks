"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from counter import views as cv
from task_3 import views as t3v
from regex import views as rev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cv.index,name="Home"),
    path('number/',cv.number,name="Counter"),
    path('register/',t3v.register,name="register"),
    path('login/',t3v.loginpage,name="login"),
    path('logout/',t3v.logoutUser,name="logout"),
    path('search/',t3v.searchUser,name="search"),
    path('regex/',rev.Regex,name="Regex"),
]
