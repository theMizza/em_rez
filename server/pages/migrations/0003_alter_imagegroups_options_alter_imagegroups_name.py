# Generated by Django 4.2.7 on 2023-11-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_staticpages_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagegroups',
            options={'verbose_name': 'Группа изображений', 'verbose_name_plural': 'Группы изображений'},
        ),
        migrations.AlterField(
            model_name='imagegroups',
            name='name',
            field=models.CharField(max_length=600, verbose_name='Название группы'),
        ),
    ]
