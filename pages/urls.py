from django.urls import path
from . import views
from .views import submit_questionnaire

# app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('values_education', views.values_education, name='values_education'),
    path('activities', views.activities, name='activities'),
    path('submit-questionnaire/', submit_questionnaire, name='submit_questionnaire'),
    path('about',views.about, name ='about'),
    path('FAQ',views.FAQ, name ='FAQ'),
]