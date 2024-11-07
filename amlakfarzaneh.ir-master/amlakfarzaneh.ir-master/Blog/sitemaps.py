from django.contrib.sitemaps import Sitemap

from django.urls import reverse

from .models import Article


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.create_date

    def location(self, item):
        return reverse('articles_detail', kwargs={'slug': item.slug})
