from django.urls import path
from . import views
from django.contrib.auth.views import LoginView # function to create login view

'''
#path('login/', LoginView.as_view(template_name='classicmodels/userLogin.html'), name="Login")

'''
'''path('admin/', admin.site.urls), #localhost:8000/admin
path('login/', LoginView.as_view(template_name='classicmodels/userLogin.html'), name="Login"),
path('', include('classicmodels.urls')),
path('menudetails/', views.menu_details_view, name='menudetails')
'''


urlpatterns = [
    path('', views.index, name='index'),
    path('classicmodels/adminedit/', views.admin_edit_view, name='adminedit')
]