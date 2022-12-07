from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'newsposts'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('news/<int:article_id>', views.detail, name = 'detail'),
    path('tags/<str:slug>', views.all_article_tags, name="all_article_tags"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)