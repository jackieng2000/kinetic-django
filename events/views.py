# events/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Event, OtherPhoto
from .forms import EventForm, OtherPhotoFormSet
from django.contrib import messages,auth

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)
        formset = OtherPhotoFormSet(request.POST, request.FILES, queryset=OtherPhoto.objects.none())
        print('In Post before form validation')
        print('form is valid: ', event_form.is_valid())
        print('formset is valid: ', formset.is_valid())
        
        if event_form.is_valid() and formset.is_valid():
            event = event_form.save(commit=False)
            event.updated_by = request.user
            print('just before event.save()')
            event.save()

            # Save each photo from the formset
            for photo_form in formset:
                other_photo = photo_form.save(commit=False)
                if other_photo.photo:  # Check if a photo was uploaded
                    other_photo.event = event
                    other_photo.save()

            return redirect('events')
        else:
            # If the form is invalid, you can print the errors for debugging
            print(event_form.errors)  # To see errors in the console
            print(formset.errors)      # To see formset errors in the console
    else:
        event_form = EventForm()
        formset = OtherPhotoFormSet(queryset=OtherPhoto.objects.none())

    return render(request, 'events/create_event.html', {
        'event_form': event_form,
        'formset': formset,
    })

def select_event(request):
    events = Event.objects.all()
    return render(request, 'events/select_event.html', {'events': events})

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    if request.method == 'POST':

        event_form = EventForm(request.POST, request.FILES, instance=event)

        formset = OtherPhotoFormSet(request.POST, 
                                    request.FILES, 
                                    queryset=event.other_photos.all())
        
        print('formset.total_form_count(): ',formset.total_form_count())
        print('form is valid: ', event_form.is_valid())
        print('formset is valid: ', formset.is_valid())

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.save()
            print('event.save()', event)

            # Save each photo from the formset
            for form in formset:
                print('form is valid: ', form.is_valid())
                form.instance.event = event 
                print('form.instance ', form.instance)
                print('form.instance.photo', form.instance.photo)
                print('form.instance.id ', form.instance.id)
                print('form.instance.sequence ', form.instance.sequence)
                print('form.instance.event ', form.instance.event)

                print('form.cleaned_data ', form.cleaned_data)
                #print('form.cleaned_data[DELETE] ', form.cleaned_data['DELETE'])
                
                if form.cleaned_data and not form.cleaned_data['DELETE']:  # Check if the form is not empty and not marked for deletion
                    photo = form.instance # Get the existing photo instance
                    print('photo.sequence ', photo.sequence)
                    print('form.cleaned_data[sequence] ', form.cleaned_data['sequence'])
                    print('form.instance.photo ', form.instance.photo)
                    #photo.event = event  # Associate with the event
                    #if not form.cleaned_data['sequence']:
                    #    photo.sequence = form.cleaned_data['sequence']  # Update only the sequence
                    #if not form.cleaned_data['photo']:
                    #    photo.instance.photo = form.cleaned_data['photo']  # Update only the sequence
                    #if not form.cleaned_data['id']:
                    #    photo.instance.id = form.cleaned_data['id']  # Update only the sequence
                    print('photo.sequence ', photo.sequence)
                    print('photo.photo ', photo.photo)
                    print('photo.id ', photo.id)
                    # photo = form.save(commit=False)  # Get the photo instance without saving
                    
                    print('photo.event ', photo.event)
                    
                    print('form.is_valid(): ', form.is_valid())
                    print('form.errors: ', form.errors)
                    if form.is_valid():
                        print('photo.save()', photo)
                        photo.save()  # Save the photo instance

            # Handle deletion of marked instances
            for form in formset:
                if form.cleaned_data.get('delete'):
                    form.instance.delete()  # Delete the instance
            

            #formset.instance = event
            # Assign the event to the formset before saving
            #for form in formset:
            #    if form.instance.pk is None:  # This means it's a new photo
            #        form.instance.event = event  # Set the event for the new photo

            #formset.save()  # Now save the formset with the correct event_id
            
             
            #return redirect('event_detail', event_id=event.id)  # Redirect to event detail page
            messages.success(request,'Event updated successfully')
            return redirect('select_event')
        else:
            # If the form is invalid, you can print the errors for debugging
            print('event_form.errors: ',event_form.errors)  # To see errors in the console
            print('formset.errors: ',formset.errors)      # To see formset errors in the console
            messages.error(request,event_form.errors)
            messages.error(request,formset.errors)

    else:
        event_form = EventForm(instance=event)
        formset = OtherPhotoFormSet(queryset=event.other_photos.all())

    context = {
        'event': event,
        'event_form': event_form,
        'formset': formset,
    }
    print('formset.total_form_count(): ',formset.total_form_count())
    return render(request, 'events/update_event.html', context)


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})