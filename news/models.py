from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    art_content = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 5))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f"{self.art_content}"
