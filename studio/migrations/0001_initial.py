# Generated by Django 3.0.2 on 2021-09-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=30, unique=True, verbose_name='Сфера деятельности')),
                ('description', models.CharField(blank=True, max_length=2000, verbose_name='Описание')),
                ('area_slug', models.SlugField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Сфера деятельности',
                'verbose_name_plural': 'Сферы деятельности',
            },
        ),
    ]
