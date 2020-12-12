from django.contrib import admin
from classicmodels.models import Admin #may need to be all caps
from classicmodels.models import Customer #idk if i need this bc only admin does login

# Register your models here.
admin.site.register(Admin)
admin.site.register(Customer)