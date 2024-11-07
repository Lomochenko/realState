from django.contrib import admin

from .models import Estate, Category


# Register your models here.

class ItemInline(admin.StackedInline):
    model = Estate
    extra = 1
    autocomplete_fields = ('category',)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'url_slug']
    inlines = [ItemInline]
    search_fields = ('title',)


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ['title', ]
