import requests
from place.models import Place
from django.conf import settings
from requests import HTTPError


def fetch_coordinates(place):

    location, created = Place.objects.get_or_create(
        address=place
    )

    if created:
        try:
            base_url = 'https://geocode-maps.yandex.ru/1.x'
            params = {'geocode': place,
                      'apikey': settings.YANDEX_API_KEY, 'format': 'json'}
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            found_places = response.json(
            )['response']['GeoObjectCollection']['featureMember']
            if len(found_places) == 0:
                return
            most_relevant = found_places[0]
            location.longitude, location.latitude = most_relevant['GeoObject']['Point']['pos'].split(
                ' ')
            location.save()
        except HTTPError:
            pass
    return location.longitude, location.latitude
