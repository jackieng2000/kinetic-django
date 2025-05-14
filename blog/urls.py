from django.urls import path
from . import views
from .views import post_list, post_detail, PostDetailView

urlpatterns = [
    path('',post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]