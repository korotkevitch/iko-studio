# Generated by Django 3.0.2 on 2021-12-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0011_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='example',
            name='area',
        ),
        migrations.RemoveField(
            model_name='example',
            name='tmpl_name',
        ),
        migrations.AddField(
            model_name='example',
            name='example_upl',
            field=models.CharField(blank=True, max_length=20, verbose_name='УРЛ сайта'),
        ),
    ]
