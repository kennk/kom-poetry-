"""kompoetry URL Configuration

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
from itanikom import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),


    # Todos - itanikom poems

    path('', views.home, name='home'),
    path('create/', views.createitanikom, name='createitanikom'),
    path('current/', views.currentitanikoms, name='currentitanikoms'),
    path('completed/', views.completeditanikoms, name='completeditanikoms'),
    path('itanikom/<int:itanikom_pk>', views.viewitanikom, name='viewitanikom'),
    path('itanikom/<int:itanikom_pk>/complete', views.completeitanikom, name='completeitanikom'),
    path('itanikom/<int:itanikom_pk>/delete', views.deleteitanikom, name='deleteitanikom'),


]
