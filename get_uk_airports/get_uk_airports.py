from collections import OrderedDict
import requests
import sys


class GetUkAirports:

    def __init__(self):
        self.locations_endpoint = "https://api.skypicker.com/locations?"
        self.headers = {"Content-type": "application/json"}
        self.airport_info = []
        self.airport_subinfo = OrderedDict()

    def __str__(self):
        row = ''
        for i in range(len(self.airport_info)):
            for n in range(len(self.airport_info[i])):
                try:
                    row += list(self.airport_info[i].values())[n] + ', '
                except TypeError:
                    row += str(list(self.airport_info[i].values())[n]) + ', '
            row += '\n '
        return row

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
                       "sort": "name"}

        try:
            response = requests.request("GET", self.locations_endpoint, headers=self.headers, params=querystring)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_error:
            print("Http Error:", http_error)
        except requests.exceptions.RequestException as request_exception:
            print('OOOPS something went badly wrong.', request_exception)
            sys.exit(1)

    def airport_get_info(self, data, iata, names, cities, coords):

        """
        Get information about UK airports from json
        :returns list of airports
        """

        for i in range(len(data['locations'])):

            if iata:
                self.airport_subinfo['iata'] = data['locations'][i]['id']
            if names:
                self.airport_subinfo['name'] = data['locations'][i]['name']
            if cities:
                self.airport_subinfo['city'] = data['locations'][i]['city']['name']
            if coords:
                self.airport_subinfo['longitude'] = data['locations'][i]['location']['lon']
                self.airport_subinfo['latitude'] = data['locations'][i]['location']['lat']

            self.airport_info.append(self.airport_subinfo)
            self.airport_subinfo = {}

        return self.airport_info
