from django.shortcuts import render

# Create your views here.


from django.urls import path

#from . models import Category, Product
from . import views


def index(request):
    
    context = {}
    return render(request, 'pages/index.html')

def contact(request):
    
    context ={}
    return render(request, 'pages/contact.html')

def about(request):
    
    context ={}
    return render(request, 'pages/about.html')
    
def FAQ(request):
    
    context ={}
    return render(request, 'pages/FAQ.html')

