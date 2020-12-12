from django.shortcuts import render
from django.http import HttpResponse

from classicmodels.models import Menu

# Create your views here.
'''
def index(request):
    return HttpResponse("hello world")
    '''

def index(request):
    return render(request, 'classicmodels/home.html')

def admin_edit_view(request):
    return render(request, 'classicmodels/confirmedorder.html')

def cust_conf_view(request):
    return render(request, 'classicmodels/customerconfirm.html')

def cust_order_view(request):
    return render(request, 'classicmodels/customerorder.html')















'''
def menu_details_view(request):
    obj = Menu.objects.get(menu_item_id = '0000')

    context = {
        'category' : obj.menu_categ,
        'price' : obj.menu_price
    }

    query_set = Menu.objects.all()
    context = {
        'object_inst' : query_set,
    }

    return render(request, '/menudetails.html', context)
'''
'''

    #return render(request, 'classicmodels/login.html') 
    # reder takes 2 args: request which is a webapp thing
    # and the path of the template containing your html file 
    # when you specify any html file django will look for a templates folder 
    # so create a folder called templates in your project folder.
    # within templates folder you will also create classicmodels sub-folder 
    # since in the path we have written classicmodels/login.html
    # and then create login.html in that folder 



    #currently, this goes directly to login page for admin... this will need to be changed to a landing page

    '''