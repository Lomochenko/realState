from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ["home_page"]

    def location(self, item):
        return reverse(item)


class StaticViewSitemap2(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "never"

    def items(self):
        return [ "add_phone_number"]

    def location(self, item):
        return reverse(item)


class StaticViewSitemap3(sitemaps.Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return ["article_page"]

    def location(self, item):
        return reverse(item)
