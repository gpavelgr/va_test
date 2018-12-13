

def get_weather_for_tomorrow(location):
    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
    lookup = weather.lookup_by_location(location)
    f = lookup.forecast[1]
    return {"high": f.high, "low": f.low, "text": f.text, "date": f.date}


def get_weather_for_tomorrow_mock(location):
    return {"high": 10, "low": 7, "text": "Rainy", "date": "14 Dec 2018"}
