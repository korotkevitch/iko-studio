# Generated by Django 3.0.2 on 2021-04-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0007_feedbackindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, verbose_name='Title страницы')),
                ('title_on_image', models.CharField(blank=True, max_length=50, verbose_name='Заголовок на главном фото')),
                ('logo', models.CharField(blank=True, max_length=30, verbose_name='Лого')),
                ('image', models.FileField(blank=True, upload_to='', verbose_name='Главное фото')),
            ],
            options={
                'verbose_name': 'Верхняя часть с фото',
                'verbose_name_plural': 'Верхняя часть с фото',
            },
        ),
        migrations.AlterModelOptions(
            name='feedbackindex',
            options={'verbose_name': ' Сообщение с Главной', 'verbose_name_plural': ' Сообщения с Главной'},
        ),
    ]
