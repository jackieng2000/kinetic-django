from django.db import models

# Create your models here.

# models.py

from django.contrib.auth.models import User

class PageAccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Allow NULL values
    path = models.CharField(max_length=255)
    accessed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_str = self.user.username if self.user else "Anonymous"
        return f"{user_str} ({self.ip_address}) accessed {self.path} on {self.accessed_at}"
