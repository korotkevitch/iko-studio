# Generated by Django 3.0.2 on 2021-12-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0019_auto_20211218_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='exampledetail',
            name='testimonial_text',
            field=models.CharField(blank=True, max_length=2000, verbose_name='Текст отзыва'),
        ),
        migrations.AddField(
            model_name='exampledetail',
            name='testimonial_title',
            field=models.CharField(blank=True, max_length=5, verbose_name='Заголовок "Отзыв" (если есть)'),
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]
