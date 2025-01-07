# events/admin.py
from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'updated_at', 'updated_by')
    search_fields = ('title',)

admin.site.register(Event, EventAdmin)