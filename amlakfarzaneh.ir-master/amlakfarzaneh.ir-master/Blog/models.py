from django.db import models
from slugify import slugify


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    title_2 = models.CharField(max_length=300, unique=True, verbose_name='عنوان انگلیسی')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان url', editable=False)
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')
    author = models.ForeignKey("User.User", on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_2, allow_unicode=True, separator='_')

        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ('id',)


class Article_Detail(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله', null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'جزییاب مقاله'
        verbose_name_plural = 'جزییاب مقالات'


class Article_link(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان لینک')
    link = models.URLField(verbose_name='آدرس لینک')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله',
                                related_name='article_link_set')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لینک مفید'
        verbose_name_plural = 'لینک های مفید'
