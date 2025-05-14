from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # make sure your model has this field