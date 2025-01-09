from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import PageAccessLog

class AccessLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.method == 'GET':  # Log only GET requests
            # Get the client's IP address from the X-Forwarded-For header
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[0]  # Get the first IP in the list
            else:
                ip_address = request.META.get('REMOTE_ADDR')  # Fallback to REMOTE_ADDR

            path = request.path
            user = request.user if request.user.is_authenticated else None
            
            PageAccessLog.objects.create(
                user=user,
                ip_address=ip_address,
                path=path,
                accessed_at=now()
            )
        
        return response