# event/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()  # Change to DateField
    description = models.TextField()
    main_photo = models.ImageField(upload_to='events/main_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
 
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('event-detail-view', kwargs={'pk': self.pk})

class OtherPhoto(models.Model):
    event = models.ForeignKey(Event, related_name='other_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='events/other_photos/')
    sequence = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['sequence']

    def __str__(self):
        return f"Photo for {self.event.title}"
    
    def get_absolute_url(self): 
        return reverse('other-photo-detail-view', kwargs={'pk': self.pk})

    
