from django.urls import path
from . import views

# при задании этого параметра включается пространстов имен, теперь нужно
# указывать префикс в ссылках {% url 'blog:url_detail' key_blog.id %}
app_name = 'blog'

urlpatterns = [
    path('', views.fx_all_blogs, name='url__all_blogs'),
    path('<int:blog_id>/', views.fx_detail, name='url_detail'),
]
