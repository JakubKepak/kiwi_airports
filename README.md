# kiwi_airports
Kiwi_airports is command line program which gets UK airports from Skypicker's api (https://docs.kiwi.com/locations/).

Used version of python is 3.6.5

**Required non-build-in libraries**:
```
requests
click (https://click.palletsprojects.com/en/7.x/)
```

## Run the program
You can specify multiple option when running the program:
- **--help** -print help message
- **--cities** -print cities of airports
- **--coords** -coordinates of each airport
- **--iata** -IATA codes
- **--names** -name of the airports
- **--full** -print all above detail

When run without option, it will print name and IATA code.
You can turn off printing IATA or name by specify option **--no-iata** or **--no-name** (--no-* option is available for all options)

```
$python kiwi_airports.py
$python kiwi_airports.py --help
$python kiwi_airports.py --full
$python kiwi_airports.py --cities --coords
```

## Output
Output is nested list of dictionaries.
