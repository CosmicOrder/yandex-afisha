from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название компании', max_length=200)
    description_short = models.TextField('Кратное описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lon = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return '{} {}'.format(self.pk, self.title)


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images',
    )
    picture = models.ImageField('Картинка')
    order = models.PositiveSmallIntegerField('Позиция', default=0)

    def __str__(self):
        if self.order:
            return '{} {}'.format(self.order, self.place.title)
        return self.place.title
