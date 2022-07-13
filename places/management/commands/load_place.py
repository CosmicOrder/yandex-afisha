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

        json_for_db = response.json()

        place, created = Place.objects.get_or_create(
            title=json_for_db['title'],
            description_short=json_for_db['description_short'],
            description_long=json_for_db['description_long'],
            lon=json_for_db['coordinates']['lng'],
            lat=json_for_db['coordinates']['lat'],
        )

        for i, img_url in enumerate(json_for_db['imgs'], 1):
            response = requests.get(img_url)
            response.raise_for_status()

            picture = ContentFile(response.content)

            image = Image.objects.create(place=place)

            image.picture.save(f'{i}.jpg', picture)
