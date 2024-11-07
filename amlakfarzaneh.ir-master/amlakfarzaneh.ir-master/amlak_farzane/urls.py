"""
URL configuration for amlak_farzane project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from Blog.sitemaps import BlogSitemap
from property.sitemaps import PropertySitemap
from .sitemaps import StaticViewSitemap, StaticViewSitemap2, StaticViewSitemap3

sitemaps = {
    "static": StaticViewSitemap,
    "static2": StaticViewSitemap2,
    "static3": StaticViewSitemap3,
    "blogs": BlogSitemap,
    "prop": PropertySitemap
}

handler404 = '404.views.error_404'
urlpatterns = [
                  path('farzaneh-dashboard/', admin.site.urls),
                  path('', include('Home.urls')),
                  path('', include('property.urls')),
                  path('', include('Blog.urls')),
                  path(
                      "sitemap.xml",
                      sitemap,
                      {"sitemaps": sitemaps},
                      name="django.contrib.sitemaps.views.sitemap",
                  ),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "داشبورد"
admin.site.index_title = "dashboard"
admin.site.site_header = "املاک فرزانه"
