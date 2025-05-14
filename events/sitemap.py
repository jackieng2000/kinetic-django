from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Event, OtherPhoto  # import your actual models

class EventsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # make sure your model has this field
    
    
class OtherPhotoSitemap(Sitemap):
    changefreq = "monthly"  # Photos might change less frequently
    priority = 0.3

    def items(self):
        return OtherPhoto.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # Using upload_date if no updated_at field
