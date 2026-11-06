from django.contrib import admin
# добавляем модели из наше созданной таблицы
from .models import Project

# нужно зарегистрировать информацию из таблицы, которую хотим видеть в панели админа
admin.site.register(Project)
