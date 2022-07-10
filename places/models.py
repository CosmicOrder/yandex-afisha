from django.db import models


class Place(models.Model):
    title = models.CharField('Название компании', max_length=200)
    description_short = models.TextField('Кратное описание')
    description_long = models.TextField('Полное описание')
    lon = models.FloatField('Долгота', null=True)
    lat = models.FloatField('Широта', null=True)

    def __str__(self):
        return f'{self.pk} ' + self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Картинка',
        related_name='images',
    )
    picture = models.ImageField('Картинка')

    def __str__(self):
        return f'{self.pk} ' + self.place.title
