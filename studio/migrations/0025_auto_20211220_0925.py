# Generated by Django 3.0.2 on 2021-12-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0024_exampledetail_hosting'),
    ]

    operations = [
        migrations.AddField(
            model_name='exampledetail',
            name='partner_prefix',
            field=models.CharField(blank=True, max_length=100, verbose_name='Префикс партнера'),
        ),
        migrations.AlterField(
            model_name='exampledetail',
            name='hosting',
            field=models.CharField(blank=True, max_length=50, verbose_name='Хостинг партнера'),
        ),
    ]
