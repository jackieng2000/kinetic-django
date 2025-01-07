# event/forms.py
from django import forms
from .models import Event, OtherPhoto
from django.forms import modelformset_factory

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_date', 'description', 'main_photo']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),  # Use date input
        }

class OtherPhotoForm(forms.ModelForm):
    class Meta:
        model = OtherPhoto
        fields = ['id', 'event', 'photo', 'sequence']

# Create a formset for OtherPhoto
OtherPhotoFormSet = modelformset_factory(OtherPhoto, form=OtherPhotoForm, extra=1,can_delete=True)

#fields=('photo','sequence', 'event') ,