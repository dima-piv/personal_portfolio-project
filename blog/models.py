from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    description = models.CharField(max_length=250)

    # для отображения в админ панели имени объектов в таблице Blog
    def __str__(self):
        return self.title
