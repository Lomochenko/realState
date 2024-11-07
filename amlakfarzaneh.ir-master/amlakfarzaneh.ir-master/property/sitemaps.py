from django.contrib.sitemaps import Sitemap
from django.db.models import Count

from django.urls import reverse

from .models import Category


class PropertySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Category.objects.annotate(products_count=Count('product_categories')).filter(
            products_count__gt=0).order_by('id')

    def lastmod(self, obj):
        return obj.create_date

    def location(self, item):
        return reverse('Estate_by_category_list', kwargs={'url_slug': item.url_slug})
