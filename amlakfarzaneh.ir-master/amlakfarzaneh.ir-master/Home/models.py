from django.db import models


# Create your models here.

class Header(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_logo = models.ImageField(upload_to='logo/', verbose_name='عکس')
    is_main = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'نام سایت'
        verbose_name_plural = 'نام سایت'

    def __str__(self):
        return self.site_name


class AboutUs(models.Model):
    title = models.CharField(max_length=128, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/', verbose_name='عکس')
    text = models.TextField(verbose_name='توضیحات')
    is_main = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'


class Footer(models.Model):
    address = models.CharField(max_length=128, verbose_name='آدرس')
    work_time = models.CharField(max_length=128, verbose_name='تایم کاری')
    instagram = models.CharField(max_length=48, verbose_name='اینستاگرام')
    phone = models.CharField(max_length=19, verbose_name='شماره ')
    is_main = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'دسترسی به ما'
        verbose_name_plural = 'دسترسی به ما'

    def __str__(self):
        return self.phone


class Advertising(models.Model):
    name = models.CharField(max_length=48, verbose_name='نام')
    phone = models.CharField(max_length=15, verbose_name='شماره')
    text = models.TextField(verbose_name='شماره')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'آگهی'
        verbose_name_plural = 'آگهی'
