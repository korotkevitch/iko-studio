# Generated by Django 3.0.2 on 2021-04-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0012_auto_20210425_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='description',
            field=models.CharField(blank=True, max_length=2000, verbose_name='Описание'),
        ),
    ]
