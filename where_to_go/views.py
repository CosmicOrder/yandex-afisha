from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def get_places_specs(place):
    features = [{
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lon, place.lat],
        },
        "properties": {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": reverse('point', args=[place.pk]),
        }
    }]

    return {
        "type": "FeatureCollection",
        "features": features,
    }


def index(request):
    places = Place.objects.all()
    context = {"places": [get_places_specs(place) for place in places]}
    return render(request, "index.html", context)


def point(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    context = {
        "title": place.title,
        "imgs": [img.picture.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }
    return JsonResponse(context,
                        json_dumps_params={"ensure_ascii": False, "indent": 2})
