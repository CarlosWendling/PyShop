from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# when the user access the index page (/products), the 'view function' will be triggered
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html')


def new(request):
    return HttpResponse('New products')

