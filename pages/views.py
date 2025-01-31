from django.shortcuts import render, redirect
from django.http import HttpResponse

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
def values_education(request):
    
    context ={}
    return render(request, 'pages/values_education.html')

def activities(request):
    
    context ={}
    return render(request, 'pages/activities.html')

def about(request):
    
    context ={}
    return render(request, 'pages/about.html')
    
def FAQ(request):
    
    context ={}
    return render(request, 'pages/FAQ.html')


def submit_questionnaire(request):
    if request.method == 'POST':
        # Process form data
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        # Add more fields as needed
        print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}")  # Example processing
        return HttpResponse("Thank you for completing the questionnaire!")
    return redirect('activities')  # Redirect if not a POST request

