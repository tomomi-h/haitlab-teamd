# Generated by Django 2.2.5 on 2019-09-09 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='kakeibo',
            options={'verbose_name': 'kakeibo', 'verbose_name_plural': 'kakeibo'},
        ),
    ]
