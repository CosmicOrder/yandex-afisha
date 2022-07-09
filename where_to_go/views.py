from django.shortcuts import render
from places.models import Place


def get_places_specs(place):
    features = []
    place_for_goejson = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [],
        },
        "properties": {
            "title": "",
            "placeId": "",
            "detailsUrl": "",
        }
    }

    features.append(place_for_goejson)
    place_for_goejson["geometry"]["coordinates"] = [place.lon, place.lat]
    place_for_goejson["properties"]["title"] = place.title
    place_for_goejson["properties"]["placeId"] = ""
    place_for_goejson["properties"]["detailsUrl"] = ""

    return {
        "type": "FeatureCollection",
        "features": features,
    }


def index(request):
    places = Place.objects.all()
    context = {"places": [get_places_specs(place) for place in places]}
    return render(request, "index.html", context)
