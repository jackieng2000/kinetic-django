# events/urls.py
from django.urls import path
from . import views
from .views import EventDetailView, OtherPhotoDetailView

urlpatterns = [
    path('', views.event_list, name='events'),
    path('create/', views.create_event, name='create_event'),
    path('select/', views.select_event, name='select_event'),
    path('update/<int:pk>', views.update_event, name='update_event'),
    path('<int:pk>', views.event_detail, name='event_detail'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail-view'),
    path('photo/<int:pk>', OtherPhotoDetailView.as_view(), name='other-photo-detail-view'),
]