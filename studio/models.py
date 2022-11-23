from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from django.utils import timezone


class ExampleList(models.Model):
    title = models.CharField('Title страницы', max_length=100)
    title_short = models.CharField('Заголовок в шапке', max_length=30)
    title_crumb = models.CharField('Название в крошках', max_length=20)
    intro_title = models.CharField('Заголовок вводной части', max_length=50)
    intro_text = models.CharField('Текст вводной части', max_length=2000)
    ps_title = models.CharField('Заголовок после фото', max_length=50)
    ps_text = models.CharField('Текст после фото', max_length=3000)

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return "Портфолио"


class ExampleDetail(models.Model):
    title               = models.CharField('Title страницы', max_length=100)
    title_short         = models.CharField('Заголовок в шапке (образец сайта, пример сайта и тп}', max_length=30)
    title_crumb         = models.CharField('Название в крошках', max_length=20)
    image               = models.FileField('Скриншот', upload_to='images/templates/500_545')
    caption             = models.CharField('Заголовок для картинки', max_length=70)
    description_short   = models.CharField('Краткое описание', max_length=500)
    description_long    = models.CharField('Подробное описание', max_length=2000)
    testimonial_text    = models.CharField('Текст отзыва', max_length=2000, blank=True)
    testimonial_author  = models.CharField('Автор отзыва', max_length=50, blank=True)
    example_url         = models.CharField('УРЛ сайта', max_length=50, blank=True)
    hosting             = models.CharField('Хостинг без "/" в конце', max_length=50, blank=True)
    partner_prefix      = models.CharField('Префикс партнера начинать с "?"', max_length=100, blank=True)
    slug                = models.SlugField(max_length=80, unique=True)
    created_date        = models.DateField('Дата создания', default=timezone.now)
    is_activated        = models.BooleanField(default=True)


    def get_url(self):
        return reverse('example_details', args=[self.slug])

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:50px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Для страницы шаблона'


    class Meta:
        verbose_name = 'Образец в портфолио'
        verbose_name_plural = 'Образцы в портфолио'
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Price(models.Model):
    landing_cost = models.CharField('Цена на создание лендинга', max_length=50, blank=True)
    site_cost = models.CharField('Цена на создание сайта', max_length=50, blank=True)
    support_cost = models.CharField('Цена на сопровождение', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Цены на услуги'
        verbose_name_plural = 'Цены на услуги'

    def __str__(self):
        return "Цены на услуги"


class ContactForm(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True)
    email = models.EmailField('Емейл', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    message = models.TextField('Сообщение', max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение, заказ'
        verbose_name_plural = 'Сообщения, заказы'

    def __str__(self):
        return self.name



# class Area(models.Model):
#     area            = models.CharField('Сфера деятельности', max_length=30, unique=True)
#     description     = models.CharField('Описание', max_length=2000, blank=True)
#     slug            = models.SlugField(max_length=20, unique=True)
#
#     def get_url(self):
#         return reverse('area', args=[self.slug])
#
#
#     class Meta:
#         verbose_name = 'Сфера деятельности'
#         verbose_name_plural = 'Сферы деятельности'
#
#     def __str__(self):
#         return self.area
#
#
# class Tmpl(models.Model):
#     area                = models.ForeignKey(Area, on_delete=models.CASCADE)
#     title               = models.CharField('Title страницы', max_length=50)
#     title_short         = models.CharField('Заголовок в шапке', max_length=15)
#     title_crumb         = models.CharField('Название в крошках', max_length=20)
#     image               = models.FileField('Изображение 500*545', upload_to='images/templates/500_545')
#     image_cat           = models.FileField('Изображение 640*420', upload_to='images/templates/640_420')
#     caption             = models.CharField('Заголовок для картинки', max_length=50)
#     description_short   = models.CharField('Краткое описание шаблона', max_length=500)
#     description_long    = models.CharField('Подробное описание шаблона', max_length=2000)
#     price               = models.CharField('Цена', max_length=20)
#     slug                = models.SlugField(max_length=50, unique=True)
#     created_date        = models.DateField('Дата создания', default=timezone.now)
#     tmpl_name           = models.CharField('Name шаблона в УРЛ', max_length=20, blank=True)
#     is_activated        = models.BooleanField(default=True)
#
#
#     def get_url(self):
#         return reverse('tmpl_details', args=[self.area.slug, self.slug])
#
#     def image_preview(self):
#         if self.image:
#             return mark_safe('<img src="%s" style="width:100px; height:110px;" />' % self.image.url)
#         else:
#             return 'No Image Found'
#
#     image_preview.short_description = 'Для страницы шаблона'
#
#     def image_cat_preview(self):
#         if self.image_cat:
#             return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image_cat.url)
#         else:
#             return 'No Image Found'
#
#     image_cat_preview.short_description = 'Для каталога'
#
#     class Meta:
#         verbose_name = 'Шаблон'
#         verbose_name_plural = 'Шаблоны'
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.title