import requests
import json


class GetUkAirports:

    def __init__(self):
        self.locations_endpoint = "https://api.skypicker.com/locations?"
        self.headers = {"Content-type": "application/json"}

    def find_uk_airports(self):
        """
        Get airports in the UK
        :returns IATA codes of the airports
        """

        querystring = {"type": "subentity",
                       "term": "GB",
                       "locale": "en-US",
                       "active_only": "True",
                       "location_types": "airport",
                       "limit": "200",
                       "sort": "name"
                      }

        response = requests.request("GET", self.locations_endpoint, headers=self.headers, params=querystring)

        for i in range(70):
            print(response.json()['locations'][i]['id'])
