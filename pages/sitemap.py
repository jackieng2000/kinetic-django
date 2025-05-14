from django.contrib.sitemaps import Sitemap
from django.urls import reverse, NoReverseMatch

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'  # Adjust as needed

    def items(self):
        return ['index', 'contact','values_education','activities']
    
    def location(self, item):
        return reverse(item)