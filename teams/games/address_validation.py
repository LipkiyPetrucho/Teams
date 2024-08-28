import googlemaps
from googlemaps import exceptions

class AddressValidator:
    def __init__(self, api_key):
        self.client = googlemaps.Client(api_key)

    def validate_address(self, address_lines, region_code=None, locality=None, enable_usps_cass=None):
        try:
            response = self.client.addressvalidation(
                {
                    "address": {"addressLines": [address_lines], "regionCode": region_code, "locality": locality},
                    "enableUspsCass": enable_usps_cass
                }
            )
            return response
        except exceptions.ApiError as e:
            # Обработка ошибок API
            return {"error": str(e)}