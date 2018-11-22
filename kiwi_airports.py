from get_uk_airports.get_uk_airports import GetUkAirports
import click


@click.command()
@click.option('--iata/--no-iata', default=True, help="Returns UK airports IATA codes")
@click.option('--names/--no-names', default=True, help="Returns UK airports names")
@click.option('--cities/--no-cities', default=False, help="Returns UK airport cities")
@click.option('--coords/--no-coords', default=False, help="Returns UK airport coordinates (long, lat)")
@click.option('--full/--no-full', default=False, help="Returns UK airport coordinates (long, lat)")
def runner(iata, names, cities, coords, full):

    if full:
        iata = True
        names = True
        cities = True
        coords = True

    get_uk_airports = GetUkAirports()
    data = get_uk_airports.get_uk_airports()

    result  = (get_uk_airports.airport_info(data, iata, names, cities, coords))

    for i in range(len(result)):
        for n in range(len(result[i])):
            print(result[i][n] + ', ', end=' ')
        print('\r')


if __name__ == "__main__":

    runner()
