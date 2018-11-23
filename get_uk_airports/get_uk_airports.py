import requests
import sys


class GetUkAirports:

    def __init__(self):
        self.locations_endpoint = "https://api.skypicker.com/locations?"
        self.headers = {"Content-type": "application/json"}

    def get_uk_airports(self):
        """
        Get airports in the UK
        :returns json of UK airports
        """

        querystring = {"type": "subentity",
                       "term": "GB",
                       "locale": "en-US",
                       "active_only": "True",
                       "location_types": "airport",
                       "limit": "2000",
                       "sort": "name"
                      }

        try:
            response = requests.request("GET", self.locations_endpoint, headers=self.headers, params=querystring)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_error:
            print("Http Error:", http_error)
        except requests.exceptions.RequestException as request_exception:
            print('OOOPS something went badly wrong.', request_exception)
            sys.exit(1)

    def airport_info(self, data, iata, names, cities, coords):

        """
        Get information about UK airports from json
        :returns list of airports
        """
        airport_info = []
        airport_subinfo = []

        for i in range(len(data['locations'])):

            if iata:
                airport_subinfo.append(data['locations'][i]['id'])
            if names:
                airport_subinfo.append(data['locations'][i]['name'])
            if cities:
                airport_subinfo.append(data['locations'][i]['city']['name'])
            if coords:
                airport_subinfo.append(data['locations'][i]['location']['lon'])
                airport_subinfo.append(data['locations'][i]['location']['lat'])

            airport_info.append(airport_subinfo)
            airport_subinfo = []

        return airport_info


