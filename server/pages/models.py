from django.db import models

# Create your models here.

class ImageGroups(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=600)
    value = models.CharField(verbose_name='Значение', max_length=600)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа изображений'
        verbose_name_plural = 'Группы изображений'


class Images(models.Model):
    name = models.CharField(verbose_name='Название', max_length=600)
    group = models.ForeignKey(ImageGroups, verbose_name='Группа',
                             related_name='group_images',
                             on_delete=models.CASCADE)
    file = models.ImageField(verbose_name='Изображение', upload_to='static_pages')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class StaticPages(models.Model):
    title = models.CharField(verbose_name='Title', max_length=600)
    meta_keywords = models.CharField(verbose_name='Meta-Keywords', max_length=900, null=True, blank=True)
    meta_description = models.TextField(verbose_name='Meta-Description', null=True, blank=True)
    template_path = models.CharField(verbose_name='Путь к шаблону', max_length=600)
    images = models.ManyToManyField(ImageGroups, verbose_name='Изображения', null=True, blank=True)
    slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статичная страница'
        verbose_name_plural = 'Статичные страницы'


class TextBlocks(models.Model):
    name = models.CharField(verbose_name='Name', max_length=600)
    value = models.TextField(verbose_name='Текст')
    page = models.ForeignKey(StaticPages,
                             verbose_name='Страница',
                             related_name='page_texts',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Текстовый блок'
        verbose_name_plural = 'Текстовые блоки'