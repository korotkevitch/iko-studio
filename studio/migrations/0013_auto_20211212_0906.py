# Generated by Django 3.0.2 on 2021-12-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0012_auto_20211212_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='example',
            old_name='example_upl',
            new_name='example_url',
        ),
        migrations.AlterField(
            model_name='example',
            name='description_long',
            field=models.CharField(max_length=2000, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='example',
            name='description_short',
            field=models.CharField(max_length=500, verbose_name='Краткое описание'),
        ),
    ]