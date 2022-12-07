from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    art_title = models.CharField('Название статьи', max_length = 200)
    tags = models.ManyToManyField("Tags", related_name="Article")
    content = models.TextField('Текст статьи')
    preview = models.TextField('Превью текст')
    author = models.CharField('Автор статьи', max_length = 200)
    source = models.CharField('Источник', max_length = 200, blank=True)
    pub_date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to = "media/", blank = True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f"{self.art_title}"

class Tags(models.Model):
    title = models.CharField('Название тега', max_length = 50)
    slug = models.SlugField(max_length = 200, unique=True)

    def __str__(self):
        return self.title