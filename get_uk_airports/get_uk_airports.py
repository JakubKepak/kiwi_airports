import requests
import json


class GetUkAirports:

    def __init__(self):
        self.locations_endpoint = "https://api.skypicker.com/locations?"
        self.headers = {"Content-type": "application/json"}

    def find_uk_airports(self):
        """
        Get airports in the UK
        :returns a list of IATA codes of the airports
        """

        querystring = {"type": "subentity",
                       "term": "GB",
                       "locale": "en-US",
                       "active_only": "True",
                       "location_types": "airport",
                       "limit": "2000",
                       "sort": "name"
                      }

        response = requests.request("GET", self.locations_endpoint, headers=self.headers, params=querystring)
        IATA_codes = []

        for i in range(len(response.json()['locations'])):
            IATA_codes.append(response.json()['locations'][i]['id'])

        return IATA_codes
