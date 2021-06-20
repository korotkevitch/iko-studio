from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from django.utils import timezone


class Area(models.Model):
    area = models.CharField('Сфера деятельности', max_length=30, blank=True)
    prefix = models.CharField('Префикс для фильтра', max_length=3, blank=True)
    description = models.CharField('Описание', max_length=2000, blank=True)
    slug = models.SlugField(max_length=20, blank=True)

    def slug_in_catalog(self):
        return f'/catalog/{self.slug}'

    def get_absolute_url(self):
        return reverse('area', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = ' Сфера деятельности'
        verbose_name_plural = ' Сферы деятельности'

    def __str__(self):
        return self.area


class Tmpl(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField('Title страницы', max_length=50, blank=True)
    title_short = models.CharField('Заголовок в шапке', max_length=15, blank=True)
    title_crumb = models.CharField('Название в крошках', max_length=20, blank=True)
    image = models.FileField('Изображение 500*545', blank=True)
    image_cat = models.FileField('Изображение 640*420', blank=True)
    caption = models.CharField('Заголовок для картинки', max_length=50, blank=True)
    description_short = models.CharField('Краткое описание шаблона', max_length=500, blank=True)
    description_long = models.CharField('Подробное описание шаблона', max_length=2000, blank=True)
    price = models.CharField('Цена', max_length=20, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    created_date = models.DateField('Дата создания', default=timezone.now)
    tmpl_name = models.CharField('Name шаблона в УРЛ', max_length=20, blank=True)

    # def slug_for_demo_btn(self):
    #     return f'/examples/{self.tmpl_name}'

    def get_absolute_url(self):
        return reverse('tmpl_details', kwargs={'tmpl_slug': self.area.slug, 'slug': self.slug })

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:110px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Для страницы шаблона'

    def image_cat_preview(self):
        if self.image_cat:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image_cat.url)
        else:
            return 'No Image Found'

    image_cat_preview.short_description = 'Для каталога'

    class Meta:
        verbose_name = ' Шаблон'
        verbose_name_plural = ' Шаблоны'
        ordering = ['-created_date']

    def __str__(self):
        return self.title



class TmpGallery(models.Model):
    prefix = models.CharField('Префикс шаблона (отрасль)', max_length=20, blank=True)
    url_name = models.CharField('name шаблона (для ссылки)', max_length=20, blank=True)
    name = models.CharField('Название шаблона', max_length=50, blank=True)
    image = models.FileField('Фото шаблона', blank=True)

    def tmp_gallery_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:110px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Галерея шаблонов'
        verbose_name_plural = 'Галерея шаблонов'

    def __str__(self):
        return self.name

    tmp_gallery_preview.short_description = 'Превью'


class Header(models.Model):
    logo = models.FileField('Логотип', blank=True)
    fon = models.FileField('Фон', blank=True)
    title = models.CharField('Заголовок', max_length=30, blank=True)
    subtitle = models.CharField('Подзаголовок', max_length=30, blank=True)
    description = models.CharField('Описание', max_length=250, blank=True)
    slide = models.FileField('Слайд', blank=True)

    def logo_preview(self):
        if self.logo:
            return mark_safe('<img src="%s" style="width:100px; height:30px;" />' % self.logo.url)
        else:
            return 'No Image Found'

    logo_preview.short_description = 'Логотип'

    def fon_preview(self):
        if self.fon:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.fon.url)
        else:
            return 'No Image Found'

    fon_preview.short_description = 'Фон'

    def slide_preview(self):
        if self.slide:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.slide.url)
        else:
            return 'No Image Found'

    slide_preview.short_description = 'Слайд'


    class Meta:
        verbose_name = ' Header'
        verbose_name_plural = ' Header'

    def __str__(self):
        return self.title


    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Скриншот'


    class Meta:
        verbose_name = ' Образец сайта'
        verbose_name_plural = ' Образцы сайтов'

    def __str__(self):
        return self.title


class FeedbackIndex(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True,)
    email = models.EmailField('Емейл', max_length=50, blank=True,)
    subject = models.CharField('Тема', max_length=50, blank=True,)
    message = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = ' Сообщение с Главной'
        verbose_name_plural = ' Сообщения с Главной'

    def __str__(self):
        return self.name


class Feedback(models.Model):
    fname = models.CharField('Имя', max_length=50, blank=True,)
    lname = models.CharField('Фамилия', max_length=50, blank=True, )
    email = models.EmailField('Емейл', max_length=50, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    template_number = models.CharField('Номер шаблона', max_length=50, blank=True,)
    massage = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = ' Сообщение'
        verbose_name_plural = ' Сообщения'

    def __str__(self):
        return self.lname


class FeedbackBuy(models.Model):
    fname = models.CharField('Имя', max_length=50, blank=True,)
    lname = models.CharField('Фамилия', max_length=50, blank=True, )
    email = models.EmailField('Емейл', max_length=50, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    template_number = models.CharField('Номер шаблона', max_length=50, blank=True,)
    massage = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = ' Заказ'
        verbose_name_plural = ' Заказы'

    def __str__(self):
        return self.lname


class FeedbackAdm(models.Model):
    fname = models.CharField('Имя', max_length=50, blank=True,)
    lname = models.CharField('Фамилия', max_length=50, blank=True, )
    email = models.EmailField('Емейл', max_length=50, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    template_number = models.CharField('Номер шаблона', max_length=50, blank=True,)
    massage = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = ' Доступ в админку'
        verbose_name_plural = ' Доступы в админку'

    def __str__(self):
        return self.lname



class Funny(models.Model):
    order_foods = models.CharField('Заказ еды', max_length=15, blank=True)
    order_phone = models.CharField('Тел. для заказа', max_length=20, blank=True)
    contact_phone = models.CharField('Контактный тел.', max_length=50, blank=True)
    email = models.CharField('Е-мейл', max_length=30, blank=True)
    name = models.CharField('Название в шапке', max_length=10, blank=True)
    head_description = models.TextField('Описание в шапке', max_length=300, blank=True)
    download_menu = models.FileField('Меню для скачивания', blank=True)
    first_title = models.CharField('Название первого раздела', max_length=15, blank=True)
    first_text = models.CharField('Текст первого раздела', max_length=550, blank=True)
    second_title = models.CharField('Название второго раздела', max_length=15, blank=True)
    second_text = models.CharField('Текст второго раздела', max_length=550, blank=True)
    address = models.CharField('Наш адрес', max_length=100, blank=True)
    work_time = models.CharField('График работы', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Funny - ресторан'
        verbose_name_plural = 'Funny - ресторан'

    def __str__(self):
        return self.name

class FunnyGallery(models.Model):
    name = models.CharField('Название блюда', max_length=20, blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)
    image = models.FileField('Фото', blank=True)

    def gallery_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Funny - галерея'
        verbose_name_plural = 'Funny - галерея'

    def __str__(self):
        return self.name


class FunnyMenuFirst(models.Model):
    name = models.CharField('Название меню', max_length=20, blank=True)
    food = models.CharField('Название блюда', max_length=40, blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    class Meta:
        verbose_name = 'Funny - меню N1'
        verbose_name_plural = 'Funny - меню N1'

    def __str__(self):
        return self.name


class FunnyMenuSecond(models.Model):
    name = models.CharField('Название меню', max_length=20, blank=True)
    food = models.CharField('Название блюда', max_length=40, blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    class Meta:
        verbose_name = 'Funny  - меню N2'
        verbose_name_plural = 'Funny  - меню N2'

    def __str__(self):
        return self.name


class FunnyMenuThird(models.Model):
    name = models.CharField('Название меню', max_length=20, blank=True)
    food = models.CharField('Название блюда', max_length=40, blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    class Meta:
        verbose_name = 'Funny  - меню N3'
        verbose_name_plural = 'Funny  - меню N3'

    def __str__(self):
        return self.name


class FunnyFeedback(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True,)
    email = models.EmailField('Емейл', max_length=50, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    massage = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = 'Funny - cообщение, заказ'
        verbose_name_plural = 'Funny - cообщения, заказы'

    def __str__(self):
        return self.name

########### Pizza ############

class PizzaInfo(models.Model):
    name = models.CharField('Название ресторана', max_length=50, blank=True, )
    about = models.CharField('О нас', max_length=500, blank=True, )
    download_menu = models.FileField('Меню для скачивания', blank=True)
    class Meta:
        verbose_name = 'Pizza - info'
        verbose_name_plural = 'Pizza - info'

    def __str__(self):
        return self.name


class PizzaImages(models.Model):
    name = models.CharField('Название картинки', max_length=50, blank=True,)
    image = models.FileField('Имя файла', blank=True)

    def pizza_images_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    pizza_images_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Pizza - изображение'
        verbose_name_plural = 'Pizza - изображения'

    def __str__(self):
        return self.name


class PizzaMenu(models.Model):
    name = models.CharField('Название блюда', max_length=25, blank=True,)
    description = models.CharField('Описание блюда', max_length=60, blank=True,)
    image = models.FileField('Имя файла', blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    def pizza_menu_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    pizza_menu_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Pizza - меню'
        verbose_name_plural = 'Pizza - меню'

    def __str__(self):
        return self.name


class PizzaPopular(models.Model):
    name = models.CharField('Название блюда', max_length=25, blank=True,)
    description = models.CharField('Описание блюда', max_length=90, blank=True,)
    image = models.FileField('Имя файла', blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    def pizza_popular_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    pizza_popular_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Pizza - хит продаж'
        verbose_name_plural = 'Pizza - хиты продаж'

    def __str__(self):
        return self.name


class PizzaGallery(models.Model):
    name = models.CharField('Название фото', max_length=20, blank=True)
    image = models.FileField('Фото', blank=True)

    def pizza_gallery_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Pizza - галерея'
        verbose_name_plural = 'Pizza - галерея'

    def __str__(self):
        return self.name

    pizza_gallery_preview.short_description = 'Превью'


class PizzaMenu12(models.Model):
    name = models.CharField('Название блюда', max_length=25, blank=True,)
    description = models.CharField('Описание блюда', max_length=60, blank=True,)
    image = models.FileField('Имя файла', blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    def pizza_menu12_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    pizza_menu12_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Pizza - меню 12'
        verbose_name_plural = 'Pizza - меню 12'

    def __str__(self):
        return self.name


class PizzaPersonal(models.Model):
    name = models.CharField('Имя, фамилия', max_length=30, blank=True,)
    position = models.CharField('Должность', max_length=20, blank=True)
    description = models.CharField('О человеке', max_length=120, blank=True,)
    image = models.FileField('Имя файла', blank=True)

    def pizza_personal_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    pizza_personal_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Pizza - персонал'
        verbose_name_plural = 'Pizza - персонал'

    def __str__(self):
        return self.position


class PizzaFeedback(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True,)
    email = models.EmailField('Емейл', max_length=50, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    massage = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = 'Pizza - cообщение, заказ'
        verbose_name_plural = 'Pizza - cообщения, заказы'

    def __str__(self):
        return self.name


########### Venue ############

class VenueText(models.Model):
    name = models.CharField('Title', max_length=30, blank=True)
    reservation_phone = models.CharField('Телефон бронирования', max_length=30, blank=True)
    download_menu = models.FileField('Меню для скачивания', blank=True)
    first_title = models.CharField('Первая фраза на картинке', max_length=30, blank=True)
    second_title = models.CharField('Вторая фраза на картинке', max_length=50, blank=True)
    third_title = models.CharField('Третья фраза на картинке', max_length=200, blank=True)
    first_text_section_1 = models.CharField('Слоган первого раздела', max_length=50, blank=True)
    second_text_section_1 = models.CharField('Заголовок первого раздела', max_length=50, blank=True)
    third_text_section_1 = models.CharField('Текст первого раздела', max_length=400, blank=True)
    first_text_section_2 = models.CharField('Слоган второго раздела', max_length=50, blank=True)
    second_text_section_2 = models.CharField('Заголовок второго раздела', max_length=50, blank=True)
    menu_slogan = models.CharField('Слоган меню', max_length=30, blank=True)
    menu_name = models.CharField('Заголовок меню', max_length=50, blank=True)
    menu_intro_1 = models.CharField('Вступительный текст 1', max_length=800, blank=True)
    menu_intro_2 = models.CharField('Вступительный текст 2', max_length=800, blank=True)
    sign_menu_slogan = models.CharField('Слоган фирм. меню', max_length=30, blank=True)
    sign_menu_name = models.CharField('Заголовок фирм. меню', max_length=50, blank=True)
    footer_text = models.CharField('Текст внизу', max_length=400, blank=True)
    footer_address = models.CharField('Адрес внизу', max_length=100, blank=True)
    footer_phone = models.CharField('Телефон внизу', max_length=50, blank=True)
    footer_email = models.EmailField('Емейл внизу', max_length=50, blank=True, )

    class Meta:
        verbose_name = 'Venue - тексты'
        verbose_name_plural = 'Venue - тексты'

    def __str__(self):
        return self.name


class VenueImage(models.Model):
    name = models.CharField('Фото', max_length=100, blank=True)
    top_fon_image = models.FileField('Верхнее фоновое фото', blank=True)
    first_image_section_1 = models.FileField('Первое фото первого раздела', blank=True)
    second_image_section_1 = models.FileField('Второе фото первого раздела', blank=True)
    video_name = models.CharField('Название видео', max_length=100, blank=True)
    video_preview = models.FileField('Превью видео', blank=True)
    video_link = models.CharField('Код видео на Ютубе', max_length=200, blank=True)
    img_1 = models.FileField('Фото для Закусок', blank=True)
    img_2 = models.FileField('Фото для Горячего', blank=True)
    img_3 = models.FileField('Фото для Десертов', blank=True)
    bottom_fon_image = models.FileField('Фото раздела Заказ столика', blank=True)

    def top_fon_image_preview(self):
        if self.top_fon_image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.top_fon_image.url)
        else:
            return 'No Image Found'

    top_fon_image_preview.short_description = 'Верхнее фоновое фото'


    def first_image_section_1_preview(self):
        if self.first_image_section_1:
            return mark_safe('<img src="%s" style="width:70px; height:100px;" />' % self.first_image_section_1.url)
        else:
            return 'No Image Found'

    first_image_section_1_preview.short_description = '1 фото 1 раздела'


    def second_image_section_1_preview(self):
        if self.second_image_section_1:
            return mark_safe('<img src="%s" style="width:70px; height:100px;" />' % self.second_image_section_1.url)
        else:
            return 'No Image Found'

    second_image_section_1_preview.short_description = '2 фото 1 раздела'


    def video_preview_preview(self):
        if self.video_preview:
            return mark_safe('<img src="%s" style="width:100px; height:50px;" />' % self.video_preview.url)
        else:
            return 'No Image Found'

    video_preview_preview.short_description = 'Превью видео'


    def first_image_section_2_preview(self):
        if self.first_image_section_2:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.first_image_section_2.url)
        else:
            return 'No Image Found'

    first_image_section_2_preview.short_description = '1 фото 2 раздела'


    def img_1_preview(self):
        if self.img_1:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.img_1.url)
        else:
            return 'No Image Found'

    img_1_preview.short_description = 'Первое фото меню'


    def img_2_preview(self):
        if self.img_2:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.img_2.url)
        else:
            return 'No Image Found'

    img_2_preview.short_description = 'Второе фото меню'


    def img_3_preview(self):
        if self.img_3:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.img_3.url)
        else:
            return 'No Image Found'

    img_3_preview.short_description = 'Третье фото меню'


    def bottom_fon_image_preview(self):
        if self.bottom_fon_image:
            return mark_safe('<img src="%s" style="width:100px; height:50px;" />' % self.bottom_fon_image.url)
        else:
            return 'No Image Found'

    bottom_fon_image_preview.short_description = 'Нижнее фоновое фото'


    class Meta:
        verbose_name = 'Venue - картинки'
        verbose_name_plural = 'Venue - картинки'

    def __str__(self):
        return self.name


class VenueMenu(models.Model):
    name = models.CharField('Название блюда', max_length=30, blank=True)
    contents_1 = models.CharField('Ингредиент 1', max_length=20, blank=True)
    contents_2 = models.CharField('Ингредиент 2', max_length=20, blank=True)
    contents_3 = models.CharField('Ингредиент 3', max_length=20, blank=True)
    contents_4 = models.CharField('Ингредиент 4', max_length=20, blank=True)
    price = models.CharField('Цена', max_length=10, blank=True)
    sign_img = models.FileField('Вид блюда', blank=True)

    def sign_img_preview(self):
        if self.sign_img:
            return mark_safe('<img src="%s" style="width:100px; height:40px;" />' % self.sign_img.url)
        else:
            return 'No Image Found'

    sign_img_preview.short_description = 'Третье фото меню'

    class Meta:
        verbose_name = 'Venue - меню'
        verbose_name_plural = 'Venue - меню'

    def __str__(self):
        return self.name


class VenueTeam(models.Model):
    slogan = models.CharField('Слоган раздела', max_length=20, blank=True)
    name = models.CharField('Заголовок раздела', max_length=20, blank=True)
    team_intro_1 = models.CharField('Текст о команде 1', max_length=800, blank=True)
    team_intro_2 = models.CharField('Текст о команде 2', max_length=800, blank=True)
    img_1 = models.FileField('Фото сотрудника 1', blank=True)
    name_1 = models.CharField('Имя сотрудника 1', max_length=50, blank=True)
    post_1 = models.CharField('Должность сотрудника 1', max_length=30, blank=True)
    img_2 = models.FileField('Фото сотрудника 2', blank=True)
    name_2 = models.CharField('Имя сотрудника 2', max_length=50, blank=True)
    post_2 = models.CharField('Должность сотрудника 2', max_length=30, blank=True)
    img_3 = models.FileField('Фото сотрудника 3', blank=True)
    name_3 = models.CharField('Имя сотрудника 3', max_length=50, blank=True)
    post_3 = models.CharField('Должность сотрудника 3', max_length=30, blank=True)
    img_4 = models.FileField('Фото сотрудника 4', blank=True)
    name_4 = models.CharField('Имя сотрудника 4', max_length=50, blank=True)
    post_4 = models.CharField('Должность сотрудника 4', max_length=30, blank=True)


    def img_1_preview(self):
        if self.img_1:
            return mark_safe('<img src="%s" style="width:80px; height:100px;" />' % self.img_1.url)
        else:
            return 'No Image Found'

    img_1_preview.short_description = 'Фото сотрудника 1'

    def img_2_preview(self):
        if self.img_2:
            return mark_safe('<img src="%s" style="width:80px; height:100px;" />' % self.img_2.url)
        else:
            return 'No Image Found'

    img_2_preview.short_description = 'Фото сотрудника 2'

    def img_3_preview(self):
        if self.img_3:
            return mark_safe('<img src="%s" style="width:80px; height:100px;" />' % self.img_3.url)
        else:
            return 'No Image Found'

    img_3_preview.short_description = 'Фото сотрудника 3'

    def img_4_preview(self):
        if self.img_4:
            return mark_safe('<img src="%s" style="width:80px; height:100px;" />' % self.img_4.url)
        else:
            return 'No Image Found'

    img_4_preview.short_description = 'Фото сотрудника 4'

    class Meta:
        verbose_name = 'Venue - команда'
        verbose_name_plural = 'Venue - команда'

    def __str__(self):
        return self.name


class VenueTestimonial(models.Model):
    slogan = models.CharField('Слоган раздела', max_length=20, blank=True)
    name = models.CharField('Заголовок раздела', max_length=20, blank=True)
    image = models.FileField('Фон отзывов', blank=True)
    testimonial = models.CharField('Отзыв', max_length=800, blank=True)
    person = models.CharField('Имя, фамилия', max_length=50, blank=True)
    who_is = models.CharField('Кто это', max_length=50, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:40px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фон отзывов'

    class Meta:
        verbose_name = 'Venue - отзыв'
        verbose_name_plural = 'Venue - отзывы'

    def __str__(self):
        return self.name


class VenueHit(models.Model):
    slogan = models.CharField('Слоган раздела', max_length=30, blank=True)
    title = models.CharField('Название раздела', max_length=30, blank=True)
    name = models.CharField('Название блюда', max_length=90, blank=True)
    image = models.FileField('Фото', blank=True)
    contents_1 = models.CharField('Ингредиент 1', max_length=20, blank=True)
    contents_2 = models.CharField('Ингредиент 2', max_length=20, blank=True)
    contents_3 = models.CharField('Ингредиент 3', max_length=20, blank=True)
    contents_4 = models.CharField('Ингредиент 4', max_length=20, blank=True)
    price = models.CharField('Цена', max_length=10, blank=True)


    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:90px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото блюда'

    class Meta:
        verbose_name = 'Venue - хит продаж'
        verbose_name_plural = 'Venue - хит продаж'

    def __str__(self):
        return self.title


class VenueFeedback(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True,)
    email = models.EmailField('Емейл', max_length=50, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    massage = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = 'Venue - cообщение, заказ'
        verbose_name_plural = 'Venue - cообщения, заказы'

    def __str__(self):
        return self.name


class VenueRes(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True,)
    phone = models.CharField('Телефон', max_length=50, blank=True,)
    date = models.CharField('Дата, время', max_length=50, blank=True, )
    number = models.CharField('Сколько персон', max_length=50, blank=True,)

    class Meta:
        verbose_name = 'Venue - бронирование'
        verbose_name_plural = 'Venue - бронирование'

    def __str__(self):
        return self.name


class VenueThanks(models.Model):
    phrase = models.CharField('Фраза после отправки формы', max_length=100, blank=True,)
    image = models.FileField('Фоновое фото', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:40px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото фона'

    class Meta:
        verbose_name = 'Venue - форма отправлена'
        verbose_name_plural = 'Venue - форма отправлена'

    def __str__(self):
        return self.phrase


########### Coffee ############

class CoffeeInfo(models.Model):
    name = models.CharField('Название кофейни', max_length=50, blank=True, )
    about = models.CharField('О нас', max_length=550, blank=True, )
    download_menu = models.FileField('Меню для скачивания', blank=True)
    class Meta:
        verbose_name = 'Coffee - info'
        verbose_name_plural = 'Coffee - info'

    def __str__(self):
        return self.name


class CoffeeFeedback(models.Model):
    first_name = models.CharField('Имя', max_length=50, blank=True,)
    second_name = models.CharField('Фамилия', max_length=50, blank=True, )
    date = models.CharField('Дата', max_length=50, blank=True, )
    time = models.CharField('Время', max_length=50, blank=True, )
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    massage = models.TextField('Сообщение', blank=True,)

    class Meta:
        verbose_name = 'Coffee - cообщение, заказ'
        verbose_name_plural = 'Coffee - cообщения, заказы'

    def __str__(self):
        return self.second_name


class CoffeeMenu(models.Model):
    name = models.CharField('Название блюда', max_length=25, blank=True,)
    description = models.CharField('Описание блюда', max_length=60, blank=True,)
    image = models.FileField('Имя файла', blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    def coffee_menu_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    coffee_menu_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Coffee - меню'
        verbose_name_plural = 'Coffee - меню'

    def __str__(self):
        return self.name


class CoffeePopular(models.Model):
    name = models.CharField('Название блюда', max_length=25, blank=True,)
    description = models.CharField('Описание блюда', max_length=90, blank=True,)
    image = models.FileField('Имя файла', blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    def coffee_popular_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    coffee_popular_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Coffee - популярное'
        verbose_name_plural = 'Coffee - популярное'

    def __str__(self):
        return self.name


class CoffeeGallery(models.Model):
    name = models.CharField('Название фото', max_length=20, blank=True)
    image = models.FileField('Фото', blank=True)

    def coffee_gallery_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Coffee - галерея'
        verbose_name_plural = 'Coffee - галерея'

    def __str__(self):
        return self.name

    coffee_gallery_preview.short_description = 'Превью'


class CoffeeMenu9(models.Model):
    name = models.CharField('Название блюда', max_length=25, blank=True,)
    description = models.CharField('Описание блюда', max_length=60, blank=True,)
    image = models.FileField('Имя файла', blank=True)
    price = models.CharField('Цена', max_length=6, blank=True)

    def coffee_menu9_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    coffee_menu9_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Coffee - меню 9'
        verbose_name_plural = 'Coffee - меню 9'

    def __str__(self):
        return self.name


class CoffeeTestimonial(models.Model):
    image = models.FileField('Фото человека', blank=True)
    testimonial = models.CharField('Отзыв', max_length=800, blank=True)
    name = models.CharField('Имя, фамилия', max_length=50, blank=True)
    who_is = models.CharField('Кто это', max_length=50, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото человека'

    class Meta:
        verbose_name = 'Coffee - отзыв'
        verbose_name_plural = 'Coffee - отзывы'

    def __str__(self):
        return self.name


########### Kusina ############


class KusinaTop(models.Model):
    name = models.CharField('Название ресторана, 15 зн.', max_length=15, blank=True, )
    title = models.CharField('Заголовок, 25 зн.', max_length=25, blank=True, )
    subtitle = models.CharField('Подзаголовок, 125 зн.', max_length=125, blank=True, )
    image = models.FileField('Картинка слайдера 1000*1300', blank=True)
    img_1 = models.FileField('1-я картинка под заголовком 800*800', blank=True)
    descr_1 = models.CharField('Текст под 1-й картинкой, 25 зн.', max_length=25, blank=True, )
    img_2 = models.FileField('2-я картинка под заголовком 800*800', blank=True)
    descr_2 = models.CharField('Текст под 2-й картинкой, 25 зн.', max_length=25, blank=True, )
    img_3 = models.FileField('3-я картинка под заголовком 800*800', blank=True)
    descr_3 = models.CharField('Текст под 3-й картинкой, 25 зн.', max_length=25, blank=True, )

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:65px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото из слайдера'

    def img_1_preview(self):
        if self.img_1:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.img_1.url)
        else:
            return 'No Image Found'

    img_1_preview.short_description = 'Фото 1'

    def img_2_preview(self):
        if self.img_2:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.img_2.url)
        else:
            return 'No Image Found'

    img_2_preview.short_description = 'Фото 2'


    def img_3_preview(self):
        if self.img_3:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.img_3.url)
        else:
            return 'No Image Found'

    img_3_preview.short_description = 'Фото 3'

    class Meta:
        verbose_name = 'Kusina - Верхний блок (слайд)'
        verbose_name_plural = 'Kusina - Верхний блок (слайды)'

    def __str__(self):
        return self.name


class KusinaAbout(models.Model):
    name = models.CharField('Название раздела, 25 зн.', max_length=25, blank=True, )
    title = models.CharField('Заголовок, 25 зн.', max_length=25, blank=True, )
    description = models.CharField('Описание, 450 зн.', max_length=450, blank=True, )
    video_preview = models.FileField('Превью видео, 800*1200', blank=True)
    video_link = models.CharField('Код видео на Ютубе', max_length=200, blank=True)
    subtitle = models.CharField('Подзаголовок для фото, 30 зн.', max_length=30, blank=True, )
    img_1 = models.FileField('1-я картинка 800*600', blank=True)
    descr_1 = models.CharField('Текст под 1-й картинкой, 20 зн.', max_length=20, blank=True, )
    img_2 = models.FileField('2-я картинка 800*600', blank=True)
    descr_2 = models.CharField('Текст под 2-й картинкой, 20 зн.', max_length=20, blank=True, )
    img_3 = models.FileField('3-я картинка 800*600', blank=True)
    descr_3 = models.CharField('Текст под 3-й картинкой, 20 зн.', max_length=20, blank=True, )

    def img_1_preview(self):
        if self.img_1:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.img_1.url)
        else:
            return 'No Image Found'

    img_1_preview.short_description = 'Фото 1'

    def img_2_preview(self):
        if self.img_2:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.img_2.url)
        else:
            return 'No Image Found'

    img_2_preview.short_description = 'Фото 2'


    def img_3_preview(self):
        if self.img_3:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.img_3.url)
        else:
            return 'No Image Found'

    img_3_preview.short_description = 'Фото 3'

    class Meta:
        verbose_name = 'Kusina - О ресторане'
        verbose_name_plural = 'Kusina - О ресторане'

    def __str__(self):
        return self.name


class KusinaStatistics(models.Model):
    name = models.CharField('Название раздела, 30 зн.', max_length=30, blank=True, )
    image = models.FileField('Фон, 1500*1000', blank=True)
    p_1_name = models.CharField('Параметр 1, 30 зн.', max_length=30, blank=True, )
    p_1_value = models.CharField('Значение 1-го параметра, 5 зн.', max_length=5, blank=True, )
    p_2_name = models.CharField('Параметр 2, 30 зн.', max_length=30, blank=True, )
    p_2_value = models.CharField('Значение 2-го параметра, 5 зн.', max_length=5, blank=True, )
    p_3_name = models.CharField('Параметр 3, 30 зн.', max_length=30, blank=True, )
    p_3_value = models.CharField('Значение 3-го параметра, 5 зн.', max_length=5, blank=True, )
    p_4_name = models.CharField('Параметр 4, 30 зн.', max_length=30, blank=True, )
    p_4_value = models.CharField('Значение 4-го параметра, 5 зн.', max_length=5, blank=True, )

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Kusina - Статистика'
        verbose_name_plural = 'Kusina - Статитстика'

    def __str__(self):
        return self.name


class KusinaMenu(models.Model):
    name = models.CharField('Название блюда', max_length=30, blank=True)
    contents_1 = models.CharField('Ингредиент 1, 20 зн.', max_length=20, blank=True)
    contents_2 = models.CharField('Ингредиент 2, 20 зн.', max_length=20, blank=True)
    contents_3 = models.CharField('Ингредиент 3, 20 зн.', max_length=20, blank=True)
    contents_4 = models.CharField('Ингредиент 4, 20 зн.', max_length=20, blank=True)
    price = models.CharField('Цена', max_length=10, blank=True)
    image = models.FileField('Вид блюда, 800*800', blank=True)


    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Kusina - Меню'
        verbose_name_plural = 'Kusina - Меню'

    def __str__(self):
        return self.name


class KusinaTestimonial(models.Model):
    testimonial = models.CharField('Отзыв, 800 зн.', max_length=800, blank=True)
    photo = models.FileField('Фото человека, 400*400', blank=True)
    person = models.CharField('Имя, фамилия, 50 зн.', max_length=50, blank=True)
    who_is = models.CharField('Кто это, 50 зн.', max_length=50, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:40px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фон отзывов'

    def photo_preview(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.photo.url)
        else:
            return 'No Image Found'

    photo_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Kusina - Отзыв'
        verbose_name_plural = 'Kusina - Отзывы'

    def __str__(self):
        return self.person


class KusinaTeam(models.Model):
    img = models.FileField('Фото, 800*900', blank=True)
    person = models.CharField('Имя, фамилия, 50 зн.', max_length=50, blank=True)
    who_is = models.CharField('Должность, 30 зн.', max_length=30, blank=True)

    def img_preview(self):
        if self.img:
            return mark_safe('<img src="%s" style="width:90px; height:100px;" />' % self.img.url)
        else:
            return 'No Image Found'

    img_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Kusina - Сотрудник'
        verbose_name_plural = 'Kusina - Сотрудники'

    def __str__(self):
        return self.person


class KusinaReservation(models.Model):
    first_name = models.CharField('Имя', max_length=50, blank=True,)
    second_name = models.CharField('Фамилия', max_length=50, blank=True, )
    date = models.CharField('Дата', max_length=50, blank=True, )
    time = models.CharField('Время', max_length=50, blank=True, )
    phone = models.CharField('Телефон', max_length=50, blank=True, )
    person = models.TextField('Персон', blank=True,)

    class Meta:
        verbose_name = 'Kusina - Бронирование'
        verbose_name_plural = 'Kusina - Бронирования'

    def __str__(self):
        return self.second_name


class KusinaNewsletter(models.Model):
    email = models.EmailField('Имя', max_length=50, blank=True,)

    class Meta:
        verbose_name = 'Kusina - Рассылка'
        verbose_name_plural = 'Kusina - Рассылка'

    def __str__(self):
        return self.email


class KusinaInsta(models.Model):
    name = models.CharField('Название фото', max_length=50, blank=True,)
    image = models.FileField('Фото, 800*800', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Kusina - Инстаграмм'
        verbose_name_plural = 'Kusina - Инстаграмм'

    def __str__(self):
        return self.name


class KusinaDownloadMenu(models.Model):
    name = models.CharField('Название', max_length=50, blank=True,)
    menu = models.FileField('Меню', blank=True)

    class Meta:
        verbose_name = 'Kusina - Меню для скачивания'
        verbose_name_plural = 'Kusina - Меню для скачивания'

    def __str__(self):
        return self.name


class BeeGallery(models.Model):
    job = models.CharField('Вид работ', max_length=20, blank=True)
    name = models.CharField('Название проекта', max_length=50, blank=True)
    image = models.FileField('Фото', blank=True)

    def bee_gallery_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Bee - галерея'
        verbose_name_plural = 'Bee - галерея'

    def __str__(self):
        return self.name

    bee_gallery_preview.short_description = 'Превью'


class ConstructoGallery(models.Model):
    name = models.CharField('Название проекта', max_length=50, blank=True)
    image = models.FileField('Фото', blank=True)

    def constructo_gallery_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:60px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Constructo - галерея'
        verbose_name_plural = 'Constructo - галерея'

    def __str__(self):
        return self.name

    constructo_gallery_preview.short_description = 'Превью'


##### BUS ######

class BusHead(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True,)
    title_on_image = models.CharField('Заголовок на главном фото', max_length=50, blank=True,)
    logo = models.CharField('Лого', max_length=30, blank=True,)
    image = models.FileField('Главное фото', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Bus - верхняя часть с фото'
        verbose_name_plural = 'Bus - верхняя часть с фото'

    def __str__(self):
        return self.logo


class BusGallery(models.Model):
    title = models.CharField('Заголовок для фото', max_length=20, blank=True)
    description = models.CharField('Описание для фото', max_length=150, blank=True)
    image = models.FileField('Фото', blank=True)

    def bus_gallery_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Bus - галерея'
        verbose_name_plural = 'Bus - галерея'

    def __str__(self):
        return self.title

    bus_gallery_preview.short_description = 'Превью'


##### TRANSPORTER ######

class TransporterHead(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True,)
    title_on_image = models.CharField('Заголовок на главном фото', max_length=50, blank=True,)
    logo = models.CharField('Лого', max_length=30, blank=True,)
    image = models.FileField('Главное фото', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Transporters - верхняя часть с фото'
        verbose_name_plural = 'Transporters - верхняя часть с фото'

    def __str__(self):
        return self.logo