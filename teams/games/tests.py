import os
from unittest import TestCase

import django
import responses
import googlemaps
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'teams.teams.settings'
django.setup()

class AddressValidationTest(TestCase):
    def setUp(self):
        self.key = settings.GMAPS_KEY
        self.client = googlemaps.Client(self.key)

    @responses.activate
    def test_simple_addressvalidation(self):
        responses.add(
            responses.POST,
            "https://addressvalidation.googleapis.com/v1:validateAddress",
            body='{"address": {"regionCode": "US","locality": "Mountain View","addressLines": "1600 Amphitheatre Pkwy"},"enableUspsCass":true}',
            status=200,
            content_type="application/json",
        )

        # Вызов метода проверки адреса
        results = self.client.addressvalidation('1600 Amphitheatre Pk', regionCode='US', locality='Mountain View', enableUspsCass=True)

        self.assertEqual(1, len(responses.calls))

        # Формируем ожидаемый URL
        expected_url = "https://addressvalidation.googleapis.com/v1:validateAddress?key=%s" % self.key

        # Сравниваем фактический и ожидаемый URL
        self.assertEqual(expected_url, responses.calls[0].request.url)
