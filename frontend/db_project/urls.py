"""db_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

    #path('login/', LoginView.as_view(template_name='classicmodels/userLogin.html'), name="Login")

    
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView # function to create login view
from classicmodels import views

urlpatterns = [
    path('admin/', admin.site.urls), #localhost:8000/admin
    path('login/', LoginView.as_view(template_name='classicmodels/userLogin.html'), name="Login"),
    path('', include('classicmodels.urls')),
    path('adminedit/', views.admin_edit_view, name='adminedit')
    path('customerconfirm/', views.cust_conf_view, name='customerconfirm')
    path('customerorder/', views.cust_order_view, name='customerorder')

]
