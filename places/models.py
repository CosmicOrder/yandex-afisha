from django.db import models
from django.forms import JSONField


class Place(models.Model):
    title = models.CharField('Название компании', max_length=200)
    imgs = models.ImageField('Картинка', blank=True)
    description_short = models.TextField('Кратное описание')
    description_long = models.TextField('Полное описание')
    coordinates = JSONField('Координаты')

    def __str__(self):
        return self.title
