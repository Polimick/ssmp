from django.contrib import admin
from .models import Article, Comment, Party, City
# Register your models here.

admin.site.register(Article)
admin.site.register(Party)
admin.site.register(City)
admin.site.register(Comment)