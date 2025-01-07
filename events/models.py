# event/models.py
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()  # Change to DateField
    description = models.TextField()
    main_photo = models.ImageField(upload_to='events/main_photos/')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class OtherPhoto(models.Model):
    event = models.ForeignKey(Event, related_name='other_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='events/other_photos/')
    sequence = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sequence']

    def __str__(self):
        return f"Photo for {self.event.title}"