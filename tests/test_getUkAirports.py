
def test_locations_key_exists(get_data):
    assert ('locations' in get_data) is True


def test_all_airports_are_in_the_uk(get_data):
    for i in range(len(get_data['locations'])):
        assert get_data['locations'][i]['city']['country']['id'] == 'GB'


# TODO write test for all used keys
