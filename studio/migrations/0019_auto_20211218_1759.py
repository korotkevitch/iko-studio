# Generated by Django 3.0.2 on 2021-12-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0018_auto_20211218_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.CharField(max_length=2000, verbose_name='Текст отзыва'),
        ),
    ]