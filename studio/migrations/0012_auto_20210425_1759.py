# Generated by Django 3.0.2 on 2021-04-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0011_area_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='description',
            field=models.CharField(blank=True, max_length=1500, verbose_name='Описание'),
        ),
    ]
