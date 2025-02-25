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
        # Initialize scores for each category
        scores = {
            'learning_attitude': 0,  # 學習態度
            'teamwork': 0,           # 團隊合作
            'leadership': 0,         # 領導才能
            'character': 0,          # 品格修養
            'empathy': 0,            # 同理心
            'responsibility': 0,     # 責任
        }

        # Process each question and update scores
        if request.POST.get('q1') == 'true':
            scores['learning_attitude'] += 3
        if request.POST.get('q2') == 'true':
            scores['learning_attitude'] += 3

        if request.POST.get('q3') == 'true':
            scores['teamwork'] += 3
        if request.POST.get('q4') == 'true':
            scores['teamwork'] += 3

        if request.POST.get('q5') == 'true':
            scores['leadership'] += 3
        if request.POST.get('q6') == 'true':
            scores['leadership'] += 3

        if request.POST.get('q7') == 'true':
            scores['character'] += 6
        if request.POST.get('q8') == 'true':
            scores['empathy'] += 3

        if request.POST.get('q9') == 'true':
            scores['empathy'] += 3
        if request.POST.get('q10') == 'true':
            scores['responsibility'] += 6

        # Responsibility (責任與孝道) remains 0 as per requirements

        calculated_scores = {
        'learning_attitude': scores['learning_attitude'],
        'teamwork': scores['teamwork'],
        'leadership': scores['leadership'],
        'character': scores['character'],
        'empathy': scores['empathy'],
        'responsibility': scores['responsibility'],
       
    }
        print(calculated_scores)
        context = {
            'submitted': True,
            'scores': calculated_scores,
        }

        # Render the template with the scores
        return render(request, 'pages/activities.html', context)
    
    # Render the template with the form for GET requests
    return render(request, 'pages/activities.html', {'submitted': False})