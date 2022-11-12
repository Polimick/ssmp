from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    art_title = models.CharField('Название статьи', max_length = 200)
    party = models.ManyToManyField("Партия", related_name="Article")
    city = models.ManyToManyField("Город", related_name="City")
    art_content = models.TextField('Текст статьи')
    karera_1 = models.CharField('Первый шаг в карьерной лестнице', max_length = 200, blank=True)
    karera_2 = models.CharField('Второй шаг в карьерной лестнице', max_length = 200, blank=True)
    karera_3 = models.CharField('Третий шаг в карьерной лестнице', max_length = 200, blank=True)
    pub_date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to = "media/", blank = True)
    vk = models.CharField('Ссылка на страницут в ВК', max_length = 200)
    ok = models.CharField('Ссылка на страницут в Однокласниках', max_length = 200)


    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 5))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f"{self.art_title}"

class Party(models.Model):
    title = models.CharField('Название партии', max_length = 50)
    slug = models.SlugField(max_length = 200, unique=True)

    def __str__(self):
        return self.title

class City(models.Model):
    title = models.CharField('География человека', max_length = 50)
    slug = models.SlugField(max_length = 200, unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    name_user =  models.ForeignKey(User, verbose_name = 'Пользователь', on_delete = models.SET_NULL, null = True)
    comment_text = models.CharField('Текст коментария', max_length = 300)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'