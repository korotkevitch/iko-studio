# Generated by Django 3.0.2 on 2021-09-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0004_auto_20210922_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmpl',
            name='is_activated',
            field=models.BooleanField(default=True),
        ),
    ]