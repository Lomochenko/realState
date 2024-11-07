from django.contrib import admin
from django.http import HttpRequest

from Blog.models import Article, Article_Detail, Article_link


class ItemInline(admin.StackedInline):
    model = Article_Detail
    extra = 2


class ItemLinkInline(admin.StackedInline):
    model = Article_link
    extra = 2


@admin.register(Article)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']
    inlines = [ItemInline, ItemLinkInline]

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)
