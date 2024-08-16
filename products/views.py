from django.http import HttpResponse
from django.shortcuts import render

# when the user access the index page (/products), the 'view function' will be triggered
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New products')

