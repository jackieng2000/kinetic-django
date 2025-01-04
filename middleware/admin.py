# logging/admin.py
from django.contrib import admin
from .models import PageAccessLog

class PageAccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'path', 'accessed_at')  # Fields to display in the list view
    list_filter = ('user', 'ip_address', 'accessed_at')          # Filter options in the admin
    search_fields = ('path', 'user__username', 'ip_address')     # Search functionality

admin.site.register(PageAccessLog, PageAccessLogAdmin)