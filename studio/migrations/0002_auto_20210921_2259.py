# Generated by Django 3.0.2 on 2021-09-21 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='area_slug',
            new_name='slug',
        ),
    ]
