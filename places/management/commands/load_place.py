import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Upload data from json files to database'

    def add_arguments(self, parser):
        parser.add_argument('url_json')

    def handle(self, *args, **options):
        response = requests.get(options['url_json'])
        response.raise_for_status()

        place_specs = response.json()

        place, created = Place.objects.get_or_create(
            title=place_specs['title'],
            description_short=place_specs['description_short'],
            description_long=place_specs['description_long'],
            lon=place_specs['coordinates']['lng'],
            lat=place_specs['coordinates']['lat'],
        )

        for i, img_url in enumerate(place_specs['imgs'], 1):
            response = requests.get(img_url)
            response.raise_for_status()

            picture = ContentFile(response.content)

            image = Image.objects.create(place=place)

            image.picture.save(f'{i}.jpg', picture)
