from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from blog.sitemap import BlogSitemap
from events.sitemap import EventsSitemap
from events.sitemap import OtherPhotoSitemap
from pages.sitemap import StaticViewSitemap

#  for robots.txt
from django.views.generic.base import RedirectView 



sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
    'events': EventsSitemap,
    'photos': OtherPhotoSitemap,
}

urlpatterns = [
    path('', include('pages.urls')),
    path('events/', include('events.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
#    path('robots.txt', include('robots.urls')),
    path('robots.txt', RedirectView.as_view(
        url=settings.STATIC_URL + 'robots.txt',  # Points to `/static/robots.txt`
        permanent=False,
    )),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,)
    #document_root=settings.MEDIA_ROOT)