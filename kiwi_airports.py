from get_uk_airports.get_uk_airports import GetUkAirports


if __name__ == "__main__":

    get_uk_airports = GetUkAirports()
    uk_airports = get_uk_airports.find_uk_airports()

    print(uk_airports)