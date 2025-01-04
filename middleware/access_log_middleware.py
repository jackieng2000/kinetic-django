# middleware.py
from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import PageAccessLog

class AccessLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.method == 'GET':  # Log only GET requests
            ip_address = request.META.get('REMOTE_ADDR')
            path = request.path
            user = request.user if request.user.is_authenticated else None
            
            PageAccessLog.objects.create(
                user=user,
                ip_address=ip_address,
                path=path,
                accessed_at=now()
            )
        
        return response