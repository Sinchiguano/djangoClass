from django.shortcuts import render
from django.shortcuts import render, HttpResponse


# Create your views here.



def product_list(request):
    products = [
        {"id": 1, "product": "Laptop", "price": 1200.50},
        {"id": 2, "product": "Smartphone", "price": 799.99},
        {"id": 3, "product": "Headphones", "price": 150.00},
        {"id": 4, "product": "Monitor", "price": 299.99},
        {"id": 5, "product": "Keyboard", "price": 75.49},
        {"id": 6, "product": "Mouse", "price": 49.99}
    ]
    return render(request, 'products_list.html',{'lists':products})


def product_update(request,product_id):
    return HttpResponse('Product update '+ 'product_id: '+str(product_id))

def product_delete(request):
    return HttpResponse('Product delete')

def product_register(request):
    return HttpResponse('Product register')

def product_create(request,day,month,year):
    return HttpResponse('Product was created '+str(day)+'-'+str(month)+'-'+str(year))