# Generated by Django 4.2.7 on 2023-11-19 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600, verbose_name='Название типа')),
                ('value', models.CharField(max_length=600, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Тип изображения',
                'verbose_name_plural': 'Типы изображения',
            },
        ),
        migrations.CreateModel(
            name='StaticPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600, verbose_name='Title')),
                ('meta_keywords', models.CharField(blank=True, max_length=900, null=True, verbose_name='Meta-Keywords')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta-Description')),
                ('template_path', models.CharField(max_length=600, verbose_name='Путь к шаблону')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('images', models.ManyToManyField(to='pages.imagegroups', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Статичная страница',
                'verbose_name_plural': 'Статичные страницы',
            },
        ),
        migrations.CreateModel(
            name='TextBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600, verbose_name='Name')),
                ('value', models.TextField(verbose_name='Текст')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_texts', to='pages.staticpages', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Текстовый блок',
                'verbose_name_plural': 'Текстовые блоки',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600, verbose_name='Название')),
                ('file', models.ImageField(upload_to='static_pages', verbose_name='Изображение')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_images', to='pages.imagegroups', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
