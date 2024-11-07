from django.db import models
from slugify import slugify


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=48, verbose_name='عنوان', )
    slug = models.SlugField(verbose_name='عنوان در url', blank=True, editable=False, allow_unicode=True)
    url_title = models.CharField(max_length=48, verbose_name='عنوان انگلیسی')
    url_slug = models.CharField(max_length=48, verbose_name='عنوان انگلیسی', editable=False, null=True, blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='عکس', null=True, blank=True)
    create_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True, separator='_')

        if not self.url_slug:
            self.url_slug = slugify(self.url_title, allow_unicode=True, separator='_')

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی فایل '
        verbose_name_plural = 'دسته بندی ها فایل ها'


class Estate(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی',
                                 related_name='product_categories', )
    title = models.CharField(max_length=128, db_index=True, verbose_name='عنوان ملک')
    image = models.ImageField(upload_to='images/', verbose_name='عکس', null=True, blank=True)
    price = models.CharField(max_length=128, verbose_name='قیمت')
    description = models.CharField(max_length=512, verbose_name='توضیحات')
    address = models.CharField(max_length=256, verbose_name='آدرس')
    area = models.CharField(max_length=48, verbose_name='متراژ', null=True, blank=True)
    room = models.PositiveSmallIntegerField(verbose_name='تعداد خواب ', null=True, blank=True)
    bath = models.PositiveSmallIntegerField(verbose_name='تعداد سرویس ', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'فایل '
        verbose_name_plural = 'فایل ها'
        ordering = ('id',)
