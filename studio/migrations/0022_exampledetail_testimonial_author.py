# Generated by Django 3.0.2 on 2021-12-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0021_auto_20211218_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='exampledetail',
            name='testimonial_author',
            field=models.CharField(blank=True, max_length=50, verbose_name='Автор отзыва'),
        ),
    ]
