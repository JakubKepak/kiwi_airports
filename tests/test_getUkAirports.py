import requests


def test_response_is_ok():
    locations_endpoint = "https://api.skypicker.com/locations?"
    headers = {"Content-type": "application/json"}

    querystring = {"type": "subentity",
                   "term": "GB",
                   "locale": "en-US",
                   "active_only": "True",
                   "location_types": "airport",
                   "limit": "2000",
                   "sort": "name"}

    response = requests.request("GET", locations_endpoint, headers=headers, params=querystring)
    assert response.status_code == 200


def test_locations_key_exists(get_data):
    assert ('locations' in get_data) is True


def test_name_key_exists(get_data):
    for i in range(len(get_data['locations'])):
        assert ('name' in get_data['locations'][i]) is True


def test_city_key_exists(get_data):
    for i in range(len(get_data['locations'])):
        assert ('city' in get_data['locations'][i]) is True


def test_name_of_city_key_exists(get_data):
    for i in range(len(get_data['locations'])):
        assert ('name' in get_data['locations'][i]['city']) is True


def test_location_of_airport_key_exists(get_data):
    for i in range(len(get_data['locations'])):
        assert ('location' in get_data['locations'][i]) is True


def test_longitude_key_exists(get_data):
    for i in range(len(get_data['locations'])):
        assert ('lon' in get_data['locations'][i]['location']) is True


def test_latitude_key_exists(get_data):
    for i in range(len(get_data['locations'])):
        assert ('lat' in get_data['locations'][i]['location']) is True


def test_all_airports_are_in_the_uk(get_data):
    for i in range(len(get_data['locations'])):
        assert get_data['locations'][i]['city']['country']['id'] == 'GB'

