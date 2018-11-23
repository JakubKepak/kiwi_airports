import pytest
from get_uk_airports.get_uk_airports import GetUkAirports


@pytest.fixture()
def get_data():
    get_uk_airports = GetUkAirports()
    data = get_uk_airports.get_uk_airports()

    return data
