from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('article/<int:article_id>', views.detail, name = 'detail'),
    path('article/<int:article_id>/leave_comment', views.leave_comment, name = 'leave_comment'),
    path('article/<int:article_id>/delete_comment', views.leave_comment, name = 'delete_comment'),
    path('party/<str:slug>', views.all_article_party, name="all_article_party")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)