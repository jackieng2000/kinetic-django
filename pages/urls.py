from django.urls import path
from . import views

# app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about',views.about, name ='about'),
    path('FAQ',views.FAQ, name ='FAQ'),
]