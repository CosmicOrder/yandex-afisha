# Generated by Django 3.2.14 on 2022-07-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название компании')),
                ('imgs', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('description_short', models.TextField(verbose_name='Кратное описание')),
                ('description_long', models.TextField(verbose_name='Полное описание')),
            ],
        ),
    ]
